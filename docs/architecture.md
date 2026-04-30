# 系统架构说明

## 核心设计
1. **多 Agent 协作**
    - DataCollectorAgent：数据采集
    - AnalysisAgent：分析与评分
    - StrategyGeneratorAgent：策略生成
    - DecisionReviewerAgent：策略评审

2. **长链推理**
    - 数据 → 分析 → 策略 → 审核 → 输出决策
    - 支持多轮因果分析与模拟

3. **可拓展性**
    - 可接入真实企业数据源
    - 可通过历史反馈自适应优化
