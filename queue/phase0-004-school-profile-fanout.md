---
task_id: phase0-004
type: phase0
tier: 1
status: todo
depends_on: [phase0-001]
lang: zh
date_added: 2026-07-13
---

# phase0-004 · 逐流派一页 profile（fan-out 生成任务）

**一句话：** 在 001 枚举完成后，为每个被确认的流派各建一个小任务，产出一页 profile。

## 交付物（对每个流派各一个后续任务）
- `/schools/<流派>/profile.md`：核心前提 / 关键文本 / 与其他流派的共享材料与分歧 / 初步 可考 印象。【living — 允许出错，随 depth-work 修正】

## 完成判据
- 本任务本身的产物是：把 001 清单里的每个流派，落成一个 `phase0-profile-<流派>` 队列文件（小粒度，一个流派一个）。
- 每个 profile 任务标注 Tier 1、lang: zh。

## 注意 / 护栏
- profile 是 Phase-0 provisional 输出；引文遵守 §1.2。
