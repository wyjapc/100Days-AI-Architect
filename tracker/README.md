# Tracker 目录

此目录存储每日结构化学习记录。

## 文件说明

- `template.json` - 每日记录的数据契约模板
- `day-{N}.json` - 具体某天的记录文件（后续自动生成）

## 数据字段说明

- `day`: 第几天（1-100）
- `date`: 日期（YYYY-MM-DD）
- `topic`: 当日学习主题
- `status`: 状态（pending/in-progress/completed/blocked）
- `prerequisites_met`: 前置条件是否满足
- `verification_script`: 验证脚本路径或命令
- `commit_hash`: 关联的 Git 提交哈希
