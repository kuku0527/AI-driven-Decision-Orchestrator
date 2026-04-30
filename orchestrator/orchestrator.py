from .agents import DataCollectorAgent, AnalysisAgent, StrategyGeneratorAgent, DecisionReviewerAgent

class DecisionOrchestratorAgent:
    def __init__(self):
        self.data_agent = DataCollectorAgent()
        self.analysis_agent = AnalysisAgent()
        self.strategy_agent = StrategyGeneratorAgent()
        self.reviewer_agent = DecisionReviewerAgent()
    
    def run_decision_pipeline(self):
        market_data = self.data_agent.collect_market_data()
        sales_data = self.data_agent.collect_sales_data()
        kpi_data = self.data_agent.collect_internal_kpi()
        
        analysis_result = self.analysis_agent.analyze(market_data, sales_data, kpi_data)
        strategy_result = self.strategy_agent.generate_strategy(analysis_result)
        review_result = self.reviewer_agent.review(strategy_result)
        
        return {
            "market_data": market_data,
            "sales_data": sales_data,
            "kpi_data": kpi_data,
            "analysis_result": analysis_result,
            "strategy_result": strategy_result,
            "review_result": review_result
        }
