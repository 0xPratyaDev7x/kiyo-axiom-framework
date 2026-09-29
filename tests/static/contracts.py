"""Developer-only static contracts; selected properties, not full schemas or policy execution."""
import json
import posixpath
import re
from urllib.parse import unquote

SKILLS = ("init", "requirement", "implement", "review", "test", "security", "architecture", "memory")
CHECKS = {"PASS", "FAIL", "NOT_RUN", "NOT_APPLICABLE", "BLOCKED"}
TASKS = {"DONE", "PARTIALLY COMPLETE", "BLOCKED", "DECISION REQUIRED"}
RISK = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
IMPACT = {"NONE", "UPDATE_REQUIRED", "CONFLICT", "NOT_ASSESSED"}
MEMORY_FIELDS = {"id", "record_type", "status", "statement", "source", "observed_date",
 "last_modified", "last_verified", "verification_status", "verification_scope",
 "uncertainty", "repository_context", "git_revision"}
AST = ("Malicious Skills", "Supply Chain Compromise", "Over-Privileged Skills",
 "Insecure Metadata", "Untrusted External Instructions", "Weak Isolation",
 "Update Drift", "Poor Scanning", "No Governance", "Cross-Platform Reuse")
AST_FIELDS = {"Risk summary", "Kiyo control IDs", "Skill/shared procedure", "Expected behavior",
 "Required evidence", "Control owner", "Residual limitations", "Test case references", "Source"}
OWNERS = {"Kiyo Markdown guidance", "Host-native security", "Developer release process", "Human organization process"}
PROCEDURES = {
 "init": ("workflows/init.md", ("templates/init/project-context.md", "templates/memory/index.md")),
 "requirement": ("workflows/requirement.md", ("templates/requirement.md",)),
 "implement": ("workflows/implement-flow.md", ("templates/short-plan.md", "templates/reports/engineering-report.md")),
 "review": ("workflows/review.md", ("templates/reports/review-finding.md", "templates/reports/review-report.md")),
 "test": ("workflows/test.md", ("templates/test-plan.md", "templates/reports/test-report.md")),
 "security": ("workflows/security.md", ("templates/reports/security-finding.md", "templates/reports/self-check-report.md")),
 "architecture": ("workflows/architecture.md", ("templates/reports/architecture-observation.md", "templates/reports/architecture-impact-report.md")),
 "memory": ("workflows/memory-lifecycle.md", ("templates/reports/memory-diff.md", "templates/reports/memory-sync-report.md", "templates/reports/memory-repair-report.md")),
}
MANDATORY = {"KIYO.md", "framework/bootstrap.md", "framework/control-index.md",
 "framework/trust-and-authority.md", "framework/context-loading.md", "framework/activation-contract.md",
 "framework/evidence-contract.md", "framework/definition-of-done.md", "framework/reporting-contract.md",
 "framework/memory-specification.md", "workflows/read-only-flow.md", "governance/human-approval.md",
 "agent-security/owasp-ast10.md"} | {p for p, _ in PROCEDURES.values()} | {
 t for _, ts in PROCEDURES.values() for t in ts}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE = chr(96)*3


class Violation(ValueError):
    def __init__(self, code, detail):
        self.code, self.detail = code, detail
        super().__init__(code + ": " + detail)


def need(ok, code, detail):
    if not ok:
        raise Violation(code, detail)


def norm(s):
    return " ".join(s.split())


def text(data, path):
    need(path in data, "REQUIRED_FILE", path)
    return data[path].decode("utf-8").replace("\r\n", "\n")


def product(data):
    return {p.removeprefix("src/kiyo/"): b for p, b in data.items()
            if p.startswith("src/kiyo/") and p.endswith(".md") and p != "src/kiyo/README.md"}


def rows(s):
    return [[v.strip().replace(chr(96), "") for v in line.split("|")[1:-1]]
            for line in s.splitlines() if line.startswith("| ") and not re.match(r"^\|[\s:|-]+\|$", line)]


def section(s, heading):
    m = re.search(r"(?m)^#{1,6} " + re.escape(heading) + r"\s*$", s)
    need(m is not None, "SECTION_MISSING", heading)
    end = re.search(r"(?m)^#{1,6} ", s[m.end():])
    return s[m.end():m.end()+end.start()] if end else s[m.end():]


def table(s, header):
    found = rows(s)
    starts = [i for i, r in enumerate(found) if r and r[0] == header]
    need(len(starts) == 1, "TABLE_HEADER", header)
    # Callers supply a section or a file with one keyed table.
    values = found[starts[0]+1:]
    need(len({r[0] for r in values}) == len(values), "TABLE_DUPLICATE", header)
    return {r[0]: r[1:] for r in values}


def frontmatter(data, path):
    m = re.match(r"^---\n([\s\S]*?)\n---\n", text(data, path))
    need(m is not None, "FRONTMATTER", path)
    fields = {}
    for line in m[1].splitlines():
        pair = re.fullmatch(r"([a-z][a-z-]*): (.+)", line)
        need(pair is not None and pair[1] not in fields, "FRONTMATTER", path + " invalid/duplicate scalar")
        fields[pair[1]] = pair[2]
    need(set(fields) == {"name", "description"}, "FRONTMATTER_FIELDS", path)
    name, desc = fields["name"], fields["description"]
    need(re.fullmatch(r"[a-z]+(?:-[a-z]+)*", name) is not None and len(name) <= 64, "SKILL_NAME", path)
    need(0 < len(desc.strip()) <= 1024 and "<" not in desc and ">" not in desc, "SKILL_DESCRIPTION", path)
    need(not re.search(r":\s|\s#|^[!&*|>'\"{}\[\]]", desc), "FRONTMATTER_SCALAR", path)
    return fields


def entries(files):
    return sorted(p for p in files if re.fullmatch(r"skills/[^/]+/SKILL.md", p))


def skill_inventory(files):
    found = entries(files)
    names = [frontmatter(files, p)["name"] for p in found]
    need(len(names) == len(set(names)), "DUPLICATE_SKILL", "duplicate native/canonical name")
    need({p.split("/")[1] for p in found} == set(SKILLS) and len(found) == 8,
         "SKILL_INVENTORY", "exactly eight public skill directories")
    need({p for p in files if p.endswith("/SKILL.md")} == set(found),
         "SKILL_INVENTORY", "unexpected nested skill entry")


def metadata(files):
    for p in entries(files):
        need(frontmatter(files, p)["name"] == p.split("/")[1], "SKILL_NAME", p + " directory mismatch")


def slug(s):
    return re.sub(r"[^\w\- ]", "", re.sub(r"<[^>]+>", "", s).strip().lower()).replace(" ", "-")


def links(files, packaged=False):
    strings = {p: b.decode().replace("\r\n", "\n") for p, b in files.items() if p.endswith(".md")}
    anchors = {p: {slug(m[1]) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", s, re.M)} for p, s in strings.items()}
    count = 0
    for p, s in strings.items():
        body = re.sub(FENCE + r"[\s\S]*?" + FENCE, "", s)
        need(not re.search(r"(?m)^\s*\[[^\]]+\]:\s*\S|<\s*(?:a|img)\s+[^>]*\b(?:href|src)\s*=", body),
             "RESOURCE_SYNTAX", p)
        for match in LINK.finditer(body):
            dest = unquote(match[1].strip().strip("<>"))
            if dest.startswith("https://"):
                continue
            need(not re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", dest) and not dest.startswith(("/", "\\"))
                 and "\\" not in dest, "RESOURCE_ESCAPE", p + " -> " + dest)
            file, _, fragment = dest.partition("#")
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(p), file)) if file else p
            scope = "/".join(p.split("/")[:2]) + "/" if packaged else ""
            need(not resolved.startswith("../") and (not packaged or resolved.startswith(scope)),
                 "RESOURCE_ESCAPE", p + " -> " + dest)
            if resolved not in files:
                code = "RESOURCE_CASE" if resolved.casefold() in {x.casefold() for x in files} else "RESOURCE_MISSING"
                raise Violation(code, p + " -> " + dest)
            need(not fragment or fragment in anchors.get(resolved, set()), "RESOURCE_ANCHOR", p + " -> " + dest)
            count += 1
    return count


def mandatory(files):
    for p in sorted(MANDATORY):
        need(p in files, "REQUIRED_FILE", p)
    graph = {}
    for p, b in files.items():
        body = re.sub(FENCE+r"[\s\S]*?"+FENCE, "", b.decode())
        graph[p] = {posixpath.normpath(posixpath.join(posixpath.dirname(p), m[1].split("#")[0]))
                    for m in LINK.finditer(body) if not m[1].startswith("https://") and m[1].split("#")[0]}
    for name, (procedure, templates) in PROCEDURES.items():
        reached, pending = set(), [f"skills/{name}/SKILL.md"]
        while pending:
            p = pending.pop()
            if p not in reached:
                reached.add(p)
                pending.extend(graph.get(p, set()) - reached)
        need({"KIYO.md", "framework/bootstrap.md", procedure, *templates} <= reached, "PROCEDURE_REACHABILITY", name)


def manifests(data, packages, builders):
    for target, builder in builders.items():
        path = "platforms/claude/.claude-plugin/plugin.json" if target == "claude" else f"platforms/{target}/plugin.json"
        source = json.loads(text(data, path))
        expected = {"name", "description"} if target == "claude" else {"$schema", "name", "description"}
        if target == "codex":
            expected.add("extensions")
        need(set(source) == expected, "MANIFEST_FIELDS", target + " unexpected/missing properties")
        need(source["name"] == "kiyo-axiom-framework" and isinstance(source["description"], str)
             and bool(source["description"].strip()), "MANIFEST_IDENTITY", target)
        payload = dict(packages[target])
        payload[".claude-plugin/plugin.json" if target == "claude" else "plugin.json"] = data[path]
        try:
            if target == "codex":
                builder.validate_manifests(source, json.loads(payload[".codex-plugin/plugin.json"]))
            elif target == "copilot":
                builder.validate_manifest(source)
            else:
                builder.validate_payload(payload)
        except (ValueError, KeyError, TypeError) as error:
            raise Violation("MANIFEST_PROPERTIES", target + ": " + str(error)) from error


def identity(files, packages):
    index = text(files, "framework/control-index.md")
    records = [r for r in rows(index) if re.fullmatch(r"KIYO-[A-Z]+-\d{3}", r[0])]
    ids = [r[0] for r in records]
    need(len(ids) == 68 and len(set(ids)) == len(ids), "CONTROL_INDEX", "68 unique stable controls")
    used = set(re.findall(r"KIYO-[A-Z]+-\d{3}", "\n".join(b.decode() for b in files.values())))
    need(used == set(ids), "CONTROL_REFERENCE", "undefined or unused control IDs")
    for r in records:
        need(len(r) == 4 and r[3] == "ACTIVE / none" and "REQ-" in r[2], "CONTROL_INDEX", r[0])
        m = LINK.search(r[1])
        need(m is not None, "CONTROL_DEFINITION", r[0])
        filename = posixpath.normpath("framework/" + m[1].split("#")[0])
        need(r[0] in text(files, filename), "CONTROL_DEFINITION", r[0])
    for skill in SKILLS:
        s = text(files, f"skills/{skill}/SKILL.md")
        need("**kiyo." + skill + "**" in s and "Canonical name: " + skill in s, "LOGICAL_ID", skill)
    for target, payload in packages.items():
        for p, b in payload.items():
            if p.endswith("plugin.json"):
                manifest = json.loads(b)
                need(manifest["name"] == "kiyo-axiom-framework", "MANIFEST_IDENTITY", target)
                need(not {"version","author","repository","license","publisher"} & set(manifest),
                     "UNAPPROVED_RELEASE_IDENTITY", target)
        for skill in SKILLS:
            for p, b in files.items():
                if not p.startswith("skills/"):
                    need(payload.get(f"skills/{skill}/references/kiyo/"+p) == b, "CONTENT_PARITY", target+"/"+p)
    return len(ids)


# Normative clause regression checks, not natural-language permission enforcement.
# Equivalent rewrites need deliberate review of the assertion and original requirement.
BOUNDARIES = {
 "workflows/read-only-flow.md": [
  "No source, test, memory, index, report-file, formatter, settings or approval-record writes are permitted by this flow.",
  "the write is outside this flow and grants no source/memory edit."],
 "skills/review/SKILL.md": [
  "This skill authorizes analysis and chat output only.",
  "Do not edit source, tests, config or Memory; create report files by default; install packages; or commit, push, stash, reset or otherwise clean up the workspace.",
  "Do not automatically run build, test, formatter, scanner, project script or application code:"],
 "skills/architecture/SKILL.md": [
  "No source, test, config, policy, Memory, ADR/decisions.md or implicit report-file writes.",
  "A requested report path is a separate scoped output write, never permission to edit the assessed project."],
 "skills/security/SKILL.md": [
  "Do not automatically scan global home/plugin inventories; read credentials or environment dumps; probe external systems; execute suspicious payloads/examples; install scanners; or auto-fix source, config, policies, Memory or native settings.",
  "Assessment output is chat unless a separate report path is authorized."],
 "skills/requirement/SKILL.md": [
  "Stop after delivery; do not write code, run tests, sync Memory or launch Implement."],
}
APPROVAL = "request only the missing approval. Do not perform dependent actions while waiting."


def readonly(files):
    for path, clauses in BOUNDARIES.items():
        s = norm(text(files, path))
        for clause in clauses:
            need(norm(clause) in s, "READ_ONLY_BOUNDARY", path)
        need(not re.search(r"\b(?:automatically (?:fix|write|sync)|may (?:write|fix|sync) without (?:request|approval))", s, re.I),
             "UNREQUESTED_WRITE", path)
    authority = norm(text(files, "framework/trust-and-authority.md"))
    need(APPROVAL in authority, "APPROVAL_BOUNDARY_MISSING", "KIYO-AUTH-003 required waiting boundary")
    need("A Markdown approval cannot override host restrictions." in authority, "APPROVAL_BOUNDARY_MISSING", "host denial")
    tests = table(section(text(files, "framework/test-mode-safety.md"), "Mode boundaries"), "Mode")
    need(set(tests) == {"assess","run","write"}, "MODE_ENUM", "Test")
    need("File/report/Memory writes, test execution" in tests["assess"][1], "READ_ONLY_BOUNDARY", "Test assess")
    need("Tracked source/test/fixture/config repair" in tests["run"][1], "READ_ONLY_BOUNDARY", "Test run")
    memory = table(section(text(files, "framework/memory-modes.md"), "Modes and completion"), "Mode")
    need(set(memory) == {"show","check","sync","repair"}, "MODE_ENUM", "Memory")
    for mode in ("show","check"):
        need(memory[mode][1].startswith("Reads and chat only; zero"), "READ_ONLY_BOUNDARY", "Memory "+mode)
    init = table(section(text(files, "skills/init/SKILL.md"), "Mode and access contract"), "Mode / access")
    need("no source, memory, config, bootstrap or report-file writes." in init["Preview / readiness / initial analysis"][0],
         "READ_ONLY_BOUNDARY", "Init preview")
    req = table(section(text(files, "skills/requirement/SKILL.md"), "Access contract"), "Mode / access")
    need(req["Default analysis/draft/brainstorm"][0].endswith("no files changed."), "READ_ONLY_BOUNDARY", "Requirement")
    need(req["Optional specification artifact"][0].startswith("Write only the specification at the path actually requested or approved;"),
         "READ_ONLY_BOUNDARY", "Requirement output")


def enums_and_examples(files, data):
    check = table(section(text(files, "framework/evidence-contract.md"), "Exact check statuses"), "Execution status")
    task = table(section(text(files, "framework/definition-of-done.md"), "Exact task statuses"), "Task status")
    need(set(check) == CHECKS and set(task) == TASKS, "STATUS_ENUM", "check/task")
    memory_rows = rows(section(text(files,"framework/memory-specification.md"), "KIYO-MEM-006 — Memory Impact at closure"))
    need({r[0] for r in memory_rows[1:]} == IMPACT, "STATUS_ENUM", "Memory impact")
    ready = table(section(text(files,"framework/requirement-readiness.md"),"Exact readiness values"),"Value")
    need(set(ready) == {"READY_FOR_IMPLEMENTATION","DECISION_REQUIRED","INSUFFICIENT_EVIDENCE"}, "STATUS_ENUM", "readiness")
    levels = {r[0] for r in rows(text(files,"governance/governance-levels.md")) if r[0].startswith("G")}
    need(levels == {"G1 Observe","G2 Assist","G3 Controlled","G4 Restricted"}, "GOVERNANCE_ENUM", "G1-G4")
    risk = rows(text(files,"governance/risk-assessment.md"))
    level_start = next(i for i,r in enumerate(risk) if r[0]=="Level")
    need({r[0] for r in risk[level_start+1:]} == RISK, "RISK_ENUM", "four levels")
    dimensions = ("Action","Target","Environment","Data sensitivity","Reversibility","Blast radius","Affected users","Uncertainty")
    need({r[0] for r in risk[1:level_start]} == set(dimensions), "RISK_DIMENSIONS", "eight dimensions")
    need({r[0] for r in rows(text(files,"governance/data-handling.md"))[1:]} ==
         {"Public","Internal","Confidential","Restricted"}, "DATA_ENUM", "classification")
    examples = text(files,"governance/decision-examples.md")
    cases = re.findall(r"(?m)^## (GOV-E\d{2})[^\n]*\n([\s\S]*?)(?=^## |\Z)",examples)
    need([c[0] for c in cases] == [f"GOV-E{i:02}" for i in range(1,19)], "EXAMPLE_INVENTORY", "governance")
    expected = ("PROCEED","DENY","PROCEED","PROCEED","HOLD","HOLD","PROCEED","HOLD","HOLD",
                "PROCEED","HOLD","DENY","HOLD","DENY","PROCEED","HOLD","PROCEED","DENY")
    for (key,body), decision in zip(cases,expected):
        m = re.search(r"Governance: \*\*(G[1-4])[^*]*\*\*\. Risk: \*\*([^*]+)\*\*\. Decision: \*\*([A-Z]+)\*\*",body)
        need(m is not None and m[2] in RISK|{"Unknown (not assigned)"} and m[3]==decision, "EXAMPLE_DECISION",key)
        need(all(re.search(r"(?m)^- "+re.escape(d)+": \S",body) for d in dimensions), "RISK_DIMENSIONS",key)
    evidence = text(data,"tests/behavioral/verification/scenarios.md")
    record = table(section(evidence,"Complete check-record illustration — EVID-01"),"Field")
    need(set(record) == {"Name","Applicability","Command/method","Inspected scope","Execution status","Observed result",
                         "Evidence location","Limitations","Baseline relation"}, "CHECK_RECORD_FIELDS","EVID-01")
    need(record["Execution status"] == ["NOT_RUN"] and record["Observed result"][0].startswith("No test execution/result"),
         "EVIDENCE_CONTRADICTION", "EVID-01: source authored but execution absent")
    examples = [r for r in rows(evidence) if re.fullmatch(r"EVID-\d{2}",r[0])]
    need(len(examples)==20 and all(len(r)==5 and r[4]=="NOT_RUN" for r in examples), "EXAMPLE_EXECUTION","EVID cases")
    need("execution NOT_RUN" in examples[0][2] and "PASS because the test exists" in examples[0][3],
         "EVIDENCE_CONTRADICTION","EVID-01 good/bad roles")


def ast_mapping(files, data):
    s = text(files,"agent-security/owasp-ast10.md")
    parts = re.findall(r"(?m)^## (AST\d{2}) ([^\n]+)\n([\s\S]*?)(?=^## |\Z)",s)
    need([(p[0],p[1]) for p in parts] == [(f"AST{i:02}",n) for i,n in enumerate(AST,1)], "AST_TAXONOMY","AST01-AST10")
    ids = set(re.findall(r"^\| (KIYO-[A-Z]+-\d{3}) \|",text(files,"framework/control-index.md"),re.M))
    scenarios = text(data,"tests/behavioral/agent-security/scenarios.md")
    for key,_,body in parts:
        fields = dict(re.findall(r"(?m)^- ([^:\n]+): ([^\n]+)",body))
        need(set(fields)==AST_FIELDS and all(fields.values()), "AST_FIELDS",key+" owner/evidence/limitations")
        need(len(fields["Residual limitations"].split())>=6, "AST_LIMITATION",key)
        owners = [part.split(":", 1) for part in fields["Control owner"].split("; ")]
        need(owners and all(len(pair)==2 and pair[0] in OWNERS and pair[1].strip() for pair in owners),
             "AST_OWNER",key)
        controls=set(re.findall(r"KIYO-[A-Z]+-\d{3}",fields["Kiyo control IDs"]))
        need(controls and controls<=ids, "AST_CONTROL",key)
        refs=re.findall(r"TC-AST-\d{2}[A-Z]?",fields["Test case references"])
        need(refs and all(r in scenarios for r in refs), "AST_CASE_REFERENCE",key)
        need("DOCUMENTED_ONLY" in fields["Source"] and re.search(r"checked \d{4}-\d{2}-\d{2}",fields["Source"]),
             "AST_SOURCE_STATUS",key)
    need("public-review draft" in s and "**ASI**" in s and "**Agentic Skills**" in s, "AST_STATUS","draft AST distinct from ASI")


def memory_templates(files):
    for name in ("project","architecture","conventions","decisions","domain","integrations","known-issues","index"):
        p=f"templates/memory/{name}.md"; s=text(files,p)
        fields=dict(re.findall(r"(?m)^- ([a-z_]+): (.*)$",s))
        need(set(fields)==MEMORY_FIELDS, "MEMORY_FIELDS",p)
        need(fields["record_type"]=="<observation | proposal | decision>" and fields["status"]=="<status valid for record_type>",
             "MEMORY_APPROVAL_DEFAULT",p)
        need(all(fields[k]=="UNKNOWN" for k in ("observed_date","last_modified","last_verified"))
             and fields["verification_status"]=="UNVERIFIED", "MEMORY_FRESHNESS_DEFAULT",p)
        need("only where actual evidence exists. No assumed approver/approval." in norm(s), "MEMORY_APPROVAL_BOUNDARY",p)
    spec=norm(text(files,"framework/memory-specification.md"))
    need("Observation: ACTIVE or ARCHIVED. Proposal: PROPOSED, REJECTED or SUPERSEDED. Decision: APPROVED, SUPERSEDED or REVOKED" in spec,
         "MEMORY_STATUS_TYPES","observation/proposal/decision")
    need("Approved decision conflicts with implementation | Architecture Drift; preserve the decision" in spec,
         "MEMORY_DECISION_DRIFT","approved intent cannot silently follow code")


def neutral_templates(files):
    paths=[p for p in files if p.startswith("templates/")]
    for p in paths:
        s=text(files,p)
        need("SYNTHETIC_PRIVATE_SENTINEL" not in s and not re.search(
            r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|(?<!\w)[A-Za-z]:[/\\]|(?<![\w/])/(?:Users|home)/[A-Za-z0-9_.-]+|praty|codejadee-framework",s,re.I),
             "TEMPLATE_SENSITIVE_CONTENT",p)
        need(not re.search(r"(?i)(?:password|api[_-]?key|token)\s*=\s*[\"']?[A-Za-z0-9_]{8,}",s),
             "TEMPLATE_SENSITIVE_CONTENT",p+" literal credential-like assignment")
        for m in re.finditer(r"(?m)^- (observed_date|last_modified|last_verified|source|statement|repository_context|git_revision): (.*)$",s):
            need(m[2]=="UNKNOWN" or m[2].startswith("<"), "TEMPLATE_PROJECT_FACT",p+":"+m[1])
        for m in re.finditer(r"(?im)^(?:- )?(?:owner|approver|provider|organization|approval_date|endpoint): (.*)$",s):
            need(m[1]=="UNKNOWN" or m[1].startswith("<"), "TEMPLATE_PROJECT_FACT",p)
    return len(paths)


def allowlist(data, packages, catalog, outputs):
    selected={p for p in data if p.startswith(("src/kiyo/","platforms/")) or p=="LICENSE"}
    need(selected==set(catalog["sources"]), "INPUT_ALLOWLIST","private/unreviewed/missing product input")
    forbidden={".git",".env",".kiyo","private","tests","tools","node_modules","hooks","mcp"}
    for target,payload in packages.items():
        for p in payload:
            need(not forbidden.intersection(p.split("/")) and not p.endswith((".py",".exe",".dll",".js",".sh",".log")),
                 "PAYLOAD_ALLOWLIST",target+"/"+p)
        need(set(payload)==set(outputs[target]), "PAYLOAD_ALLOWLIST",target+" inventory")


def budgets(files, packages):
    core=text(files,"KIYO.md")+text(files,"framework/bootstrap.md")
    need(len(core.splitlines())<=120 and len(core.split())<=600, "CONTEXT_BUDGET","bootstrap")
    for label,mapping in (("canonical",files),*packages.items()):
        for p in entries(mapping):
            s=text(mapping,p)
            need(len(s.splitlines())<=250 and len(s.split())<=1200, "CONTEXT_BUDGET",label+"/"+p)
    block=re.search(FENCE+r"markdown\n([\s\S]*?)"+FENCE,text(files,"framework/init-activation.md"))[1]
    need(len(block.split())+40<=250, "CONTEXT_BUDGET","neutral block plus native sentence reserve")
    return {"bootstrap_lines":len(core.splitlines()),"bootstrap_words":len(core.split())}


def substance(files):
    for p,b in files.items():
        s=b.decode()
        need(not re.fullmatch(r"[\s#>*-]*(?:(?:TODO|TBD|PLACEHOLDER|COMING SOON)[.!:\s#>*-]*)+",s,re.I)
             and len(re.findall(r"\w+",s))>=35, "TODO_ONLY",p)
    headings={
      "init":("Mode and access contract","Procedure and conditional references","Completion and output"),
      "requirement":("Access contract","Shared workflow and conditional references","Completion"),
      "implement":("Preconditions and access","Daily workflow","Sensitive effects and completion"),
      "review":("Input and authority","Procedure"),
      "test":("Select the requested effects","Mode-specific work","Report and complete"),
      "security":("Scope and access","Assessment and evidence"),
      "architecture":("Scope and effects","Analysis and outputs"),
      "memory":("Select intent and scope","Workflow","Boundaries and reporting")}
    for name,values in headings.items():
        for heading in values:
            body=section(text(files,f"skills/{name}/SKILL.md"),heading)
            need(len(re.findall(r"\w+",body))>=20, "REQUIRED_SECTION_EMPTY",name+"/"+heading)


def requirements(data):
    s=text(data,"docs/build/REQUIREMENTS.md")
    ids=re.findall(r"^## (REQ-\d{3})$",s,re.M)
    expected=[f"REQ-{i:03}" for i in range(1,81)]
    need(len(ids)==len(set(ids)), "REQUIREMENT_DUPLICATE","registry")
    need(ids==expected, "REQUIREMENT_INVENTORY","REQ-001 through REQ-080")
    fields=("Objective","Scope","Observable acceptance criteria","Dependencies","Planned implementation area","Planned verification")
    for key,body in zip(ids,re.split(r"(?m)^## REQ-\d{3}\n",s)[1:]):
        need(all(re.search(r"(?m)^- \*\*"+re.escape(f),body) for f in fields), "REQUIREMENT_FIELDS",key)
    trace=[r for r in rows(text(data,"docs/build/TRACEABILITY.md")) if re.fullmatch(r"REQ-\d{3}",r[0])]
    need([r[0] for r in trace]==expected and all(len(r)==10 for r in trace), "TRACEABILITY_INVENTORY","one full row per requirement")
    need(all(r[7] in {"NOT_IMPLEMENTED","PARTIALLY_IMPLEMENTED","IMPLEMENTED"} and r[8]=="NOT_RUN" for r in trace),
         "TRACEABILITY_STATUS","static subset cannot promote full verification")
