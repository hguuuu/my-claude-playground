---
task_id: phase0-002
type: phase0
tier: 1
status: todo  # redo requirements set 2026-07-29; launch awaits researcher go
depends_on: []
lang: zh
date_added: 2026-07-13
---

# phase0-002 · 一手文献可得性与存续清查

**一句话：** 盘点哪些一手文献实际可得、以何种形态可得（ctext.org、扫描本、版本），做一次可靠性&历史存续的初步 sourcing。

## 交付物
- 主要文献清单：书名 / 大致成书年代 / 作者及作者争议（如 滴天髓）/ 可得形态（ctext 链接、扫描、researcher 提供）/ 原文与注释层的可得性。
- 每项一句「存续形态」判断：该方法/文本以何种形式留存至今、经过几层注释。

## 完成判据
- 结果沉淀为 `/sources/INDEX.md` 的 intake 待办；可即刻获取的文本登记为后续 `intake:` 任务。
- 每条目标注 `verification` 与 `source_layer`（原文 / 注释 / modern）。

## 重做要求（2026-07-29 补，依 s0009 采纳决策与 meta-001 度量）
- **三分可得性判定**：agent 可直接取得 / 须研究者提供 / 目前不可得——逐文本明判。
- **每个来源入登记册**（`/sources/register/`）并带 RELIABILITY 标签（Class×Access×旗标）。
- **相对分级依 credibility 决策**（`/log/decisions/2026-07-28-source-credibility-principle.md`）：传承可信度分级＋视角来源，不设绝对真值。
- **完成后与 v0 对照**：撤回的 v0 产出（参考分支 `8a9ccec`）作为盲对照——先独立完成，再 diff 记录异同（v0 不可引用、不可作依据）。

## 注意 / 护栏
- 收敛式多源印证本身即 **可考** 轴证据（§4）——记录一条规则在多文献中的出现，不是流水账。
- 不得凭记忆「重建」经典引文（本项目最严重失败模式，§1.2）。
