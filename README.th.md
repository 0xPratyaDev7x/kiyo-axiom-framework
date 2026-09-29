# Kiyo Axiom Framework
[English](README.md) | **ภาษาไทย**

**ให้ AI coding agent ทำงานแบบวิศวกรมืออาชีพ: อ่านโปรเจกต์จริงก่อนลงมือ แก้แค่ที่สั่ง และรายงานตามหลักฐานจริง**

📖 **อ่านเอกสารฉบับเต็มได้ที่ [https://kiyo-axiom.codejadee.com](https://kiyo-axiom.codejadee.com/)**

Kiyo เป็นชุด Skill แบบ Markdown สำหรับ Claude Code, Codex และ GitHub Copilot
ติดตั้งแล้วใช้ได้ทันที ไม่มี runtime, MCP, hook, database หรือ watcher ให้ดูแลเพิ่ม

---

## ทำไมต้องใช้ Kiyo

ถ้าเคยเจอ AI agent แบบนี้ Kiyo ช่วยได้:

| ปัญหาที่เจอบ่อย | Kiyo ช่วยอย่างไร |
| --- | --- |
| 🤔 **เดาเอาเอง** ว่าโปรเจกต์ใช้ stack อะไร มี convention แบบไหน | อ่านโค้ด เอกสาร และ test จริงก่อน แยก *ข้อเท็จจริง / สมมติฐาน / ข้อเสนอ / สิ่งที่ยังไม่รู้* ให้ชัด |
| ✂️ **แก้เกินที่สั่ง** เช่น ขอแก้บั๊กเดียวแต่ refactor ทั้งไฟล์ | จำกัดขอบเขตการเปลี่ยนแปลงให้พอดีกับงาน และเก็บงานของคุณที่ไม่เกี่ยวข้องไว้เหมือนเดิม |
| ✅ **อ้างว่ารัน test ผ่าน** ทั้งที่ไม่ได้รัน | รายงานสถานะตามจริง: `PASS` / `FAIL` / `NOT_RUN` / `BLOCKED` พร้อมหลักฐาน |
| 🔧 **ขอแค่ review แต่ดันไปแก้โค้ด** | Review, Security และ Architecture เป็นแบบ read-only ตรวจแล้วรายงาน ไม่แตะโค้ด |
| 🧠 **ลืม context** ทุกครั้งที่เปิด session ใหม่ | Project Memory เก็บ context ของโปรเจกต์ไว้ใน repo และตรวจ drift เทียบกับโค้ดปัจจุบันได้ |
| ⚠️ **ทำ action อันตราย** เช่น push, deploy, แก้ production DB | มี governance และ human approval กำกับ ไม่ commit/push/deploy เองถ้าไม่ได้สั่ง |

**สรุปสั้น ๆ:** agent ทำงานได้คาดเดาง่ายขึ้น ตรวจสอบได้ และปลอดภัยกับ codebase ของทีมมากขึ้น

### สี่เสาหลัก

| เสาหลัก | ใช้ทำอะไร |
| --- | --- |
| **Project Intelligence** | เข้าใจโปรเจกต์จากหลักฐานจริง, Project Memory, ตรวจ drift |
| **Software Engineering** | Requirement, implement แบบ minimal, review, test |
| **AI Governance** | ขอบเขตงาน, ความเสี่ยง, การจัดการข้อมูล, การอนุมัติโดยมนุษย์ |
| **Agentic Skill Security** | ความน่าเชื่อถือและที่มาของ Skill, กัน prompt injection |

---

## 🚀 เริ่มใช้งานใน 3 ขั้นตอน

### 1. ติดตั้ง

repo นี้เป็น custom marketplace อยู่แล้ว เลือกคำสั่งตาม host ที่ใช้

**Claude Code** (CLI / VS Code)
```text
/plugin marketplace add 0xPratyaDev7x/kiyo-codejadee-framework
/plugin install kiyo-axiom-framework@kiyo-axiom-framework
```

**Codex (CLI / VS Code)**
```text
codex plugin marketplace add 0xPratyaDev7x/kiyo-codejadee-framework
codex plugin add kiyo-axiom-framework@kiyo-axiom-framework
```

**GitHub Copilot** (CLI / VS Code)
```text
copilot plugin marketplace add 0xPratyaDev7x/kiyo-codejadee-framework
copilot plugin install kiyo-axiom-framework@kiyo-axiom-framework
```

**Codex IDE Extension (VS Code)** โหลด plugin ไม่ได้ ให้ copy โฟลเดอร์ `kiyo-*`
ทั้งแปดโฟลเดอร์จาก `dist/codex-ide/.agents/skills/` ไปไว้ที่ `.agents/skills/` ของ repo
(หรือ `$HOME/.agents/skills/` ถ้าจะใช้ทุกโปรเจกต์) แล้วเปิดแชทใหม่
([ขั้นตอนละเอียด](platforms/codex-ide/README.md))

> ตัวเลือกอื่น เช่น ZIP สำหรับทดลองแบบ session เดียว ดูที่
> [คู่มือติดตั้ง](docs/user/README.md#install-or-load-a-prepared-package)

### 2. รัน Init เพื่อให้ Kiyo รู้จักโปรเจกต์

เรียก Skill **Init** (วิธีเรียกของแต่ละ host อยู่ในหัวข้อ “เรียก Skill ยังไง” ด้านล่าง) แล้วเริ่มจากโหมด preview ก่อน:

```text
Preview onboarding for this repository; report evidence, unknowns and proposed
Memory/config/bootstrap changes without writing files.
```

ถ้าพอใจกับผล preview ก็สั่งต่อ:

```text
Create the proposed local Memory/config; preserve existing instructions.
```

ค่าเริ่มต้น Kiyo จะสร้าง Memory ไว้ที่ `.kiyo/memory` และ config ที่ `.kiyo/policy.md`
โดยไม่แตะ source code, test หรือ dependency ของคุณ

### 3. ใช้งานประจำวัน

เลือก Skill ให้ตรงกับงาน บอกเป้าหมายและขอบเขตที่อนุญาต แล้วอ่านรายงานที่ได้
พิมพ์ภาษาไทยได้เลย Kiyo ตอบกลับตามภาษาที่คุณใช้

---

## 📋 Cheatsheet: Skill ทั้ง 8 ตัว

| Skill | ใช้เมื่อ | ตัวอย่าง prompt | แก้ไฟล์ได้ไหม |
| --- | --- | --- | --- |
| **Init** | เริ่มใช้กับโปรเจกต์ใหม่ หรืออยากให้ Kiyo วิเคราะห์โปรเจกต์ | “Preview onboarding only.” | preview: ❌ / initialize: เฉพาะ Memory/config |
| **Requirement** | แปลงคำขอดิบหรือ issue เป็น requirement ที่พร้อมทำ | “เพิ่ม export Excel ช่วยหาว่ายังขาด field หรือ permission อะไร” | ❌ ตอบในแชท (เขียนไฟล์เฉพาะ path ที่ขอ) |
| **Implement** | เพิ่ม feature, แก้บั๊ก, refactor ที่ระบุขอบเขตชัด | “Fix the boundary error and add its regression test.” | ✅ เฉพาะโค้ด/test/docs ในขอบเขต |
| **Review** | ตรวจ diff, ไฟล์, commit หรือ PR | “Review my unstaged changes; do not edit.” | ❌ read-only |
| **Test** | หา test gap, รัน test, หรือเขียน test | “Assess authorization test gaps in this module.” | แล้วแต่โหมด (ดูด้านล่าง) |
| **Security** | ตรวจความเสี่ยงของโค้ด, Skill หรือ policy | “Assess this handler for validation and authorization risks.” | ❌ read-only |
| **Architecture** | คำถามเชิงออกแบบ, วิเคราะห์ผลกระทบ, ตรวจ drift จาก ADR | “Compare ADR-007 with this module; report deviations only.” | ❌ read-only |
| **Memory** | ดู, ตรวจ, sync หรือซ่อม Project Memory | “Compare these Memory observations with this branch.” | show/check: ❌ / sync/repair: เฉพาะ entry ที่อนุญาต |

### โหมดย่อยที่ควรรู้

| Skill | โหมด | ทำอะไร |
| --- | --- | --- |
| Init | `preview` | อ่านอย่างเดียว รายงานสิ่งที่พบและสิ่งที่จะเสนอให้สร้าง |
| Init | `initialize` | สร้าง/อัปเดต Memory, config และ bootstrap ที่อนุญาต |
| Test | `assess` | อ่าน test แล้วหาช่องว่าง ไม่เขียนไฟล์ ไม่รันอะไร |
| Test | `run` | รัน test suite ที่มีอยู่หลังตรวจ script และ environment แล้ว ไม่แก้ source/test |
| Test | `write` | เขียน test ตามเคสที่ตกลงกัน (การเขียนไม่ได้แปลว่าอนุญาตให้รันด้วย) |
| Security | `application` / `skills` / `governance` / `self-check` | ตรวจโค้ดแอป / ตรวจ Skill package ตาม AST01–AST10 / ตรวจ policy / ตรวจตัว Kiyo เอง |
| Memory | `show` / `check` | สรุป entry / เทียบ Memory กับโค้ดปัจจุบันเพื่อหา drift (ไม่เขียนไฟล์) |
| Memory | `sync` / `repair` | อัปเดตเฉพาะ observation ที่มีหลักฐาน / ซ่อมลิงก์ที่ย้ายไฟล์ (เก็บ decision และประวัติไว้) |

### เรียก Skill ยังไง

slug ทั้งแปดคือ `init`, `requirement`, `implement`, `review`, `test`, `security`, `architecture`, `memory`

| Host | วิธีเรียก (ตัวอย่างใช้ `init`) |
| --- | --- |
| Claude Code CLI / VS Code | `/kiyo-axiom-framework:init` |
| Codex CLI | เปิด `/skills` หรือ `$` picker แล้วเลือก entry ของ Kiyo |
| Codex IDE Extension | `$kiyo-init` หรือเลือกจาก `/skills` |
| GitHub Copilot CLI | `/skills list` หรือ `/skills info` เพื่อหา selector ของ Kiyo |
| GitHub Copilot VS Code | `/kiyo-axiom-framework:init` หรือเลือกใน Configure Skills |

> ระวังอย่าสับสนกับคำสั่ง built-in ของ host อย่าง `/init` หรือ `/review`

### อ่านรายงานให้เป็น

| ป้าย | ความหมาย |
| --- | --- |
| `PASS` / `FAIL` | รันการตรวจจริงแล้ว ผ่าน / ไม่ผ่าน |
| `NOT_RUN` | ยังไม่ได้รัน (ไม่ใช่ “ผ่าน”) |
| `NOT_APPLICABLE` | ไม่เกี่ยวกับงานนี้ |
| `BLOCKED` | ทำต่อไม่ได้ เช่น ไม่มี environment หรือไม่มีสิทธิ์ |
| `DONE` / `PARTIALLY COMPLETE` / `DECISION REQUIRED` | สถานะของงาน: เสร็จ / เสร็จบางส่วน / ต้องให้คุณตัดสินใจก่อน |

Requirement มีสถานะความพร้อมอีกชุด: `READY_FOR_IMPLEMENTATION`, `DECISION_REQUIRED`,
`INSUFFICIENT_EVIDENCE` (สถานะ READY ไม่ได้แปลว่าให้เริ่มเขียนโค้ดเอง ต้องสั่ง Implement ต่อ)

### เคล็ดลับ

- **ระบุเป้าหมายและขอบเขตทุกครั้ง** เช่น “แก้เฉพาะไฟล์เหล่านี้” หรือ “ห้ามแก้ไฟล์”
- **คำขอกำกวมจะเริ่มแบบ read-only** เช่น “ดู login ให้หน่อย” Kiyo จะตรวจหรือถามก่อน ไม่แก้ทันที
- **เรียก Skill ให้ชัดเจน** คือวิธีที่แน่นอนที่สุด (Init ใส่ routing hint ให้ host เลือก Skill เองได้ แต่ยังไม่แน่นอน 100%)
- **ต้องการคำตอบภาษาอื่น** ให้บอก “answer in English” ส่วนโค้ด คำสั่ง และ path จะคงเดิม

---

## 📚 เอกสาร

**เอกสารฉบับเต็ม: [https://kiyo-axiom.codejadee.com/](https://kiyo-axiom.codejadee.com/)**

คู่มือใน repo:

- [คู่มือผู้ใช้: ติดตั้ง → Init → ใช้งานประจำวัน → รายงาน](docs/user/README.md)
- [รายละเอียด input, โหมด และขอบเขตของแต่ละ Skill](docs/user/skills.md)
- [Governance และการอนุมัติ](docs/user/governance.md)
- [Memory และ drift](docs/user/memory.md)
- [Security ของแอปและของ agent](docs/user/security.md)
- [Troubleshooting](docs/user/troubleshooting.md)
- [ตัวอย่าง walkthrough 9 แบบ](docs/user/walkthroughs.md)
- [คู่มือสำหรับ maintainer](docs/developer/maintainer-guide.md)

---

## สถานะโปรเจกต์

Kiyo อยู่ในช่วง **development preview** (ชื่อยังเป็น working name และยังไม่มี public release)
ติดตั้งผ่าน marketplace ของ repo นี้ได้ แต่การทดสอบ agent workflow แบบเต็มบนทุก host ยังไม่เสร็จ

- Kiyo เป็นแนวทางให้ agent ทำตาม ส่วนสิทธิ์และการรันคำสั่งยังเป็นของ host
  Kiyo ไม่ได้ทำ sandbox และไม่รับประกันว่า agent จะทำตามทุกครั้ง
- ไม่ได้รับรอง ISO/OWASP compliance หรือนโยบาย privacy ของ provider ใด ๆ
- ผลทดสอบรายละเอียดของแต่ละ host: [compatibility matrix](docs/compatibility/live-test-matrix.md)
  และ [Final Acceptance Report](docs/build/FINAL-ACCEPTANCE.md)

## License

[MIT](LICENSE)
