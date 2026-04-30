import random

class DataCollectorAgent:
    def collect_market_data(self):
        return {"trend": random.choice(["up", "down", "stable"]), "volume": random.randint(50, 150)}
    
    def collect_sales_data(self):
        return {"sales_last_quarter": random.randint(1000, 5000)}

    def collect_internal_kpi(self):
        return {"employee_efficiency": random.uniform(0.7, 1.0)}

class AnalysisAgent:
    def analyze(self, market_data, sales_data, kpi_data):
        score = 0
        if market_data["trend"] == "up":
            score += 2
        elif market_data["trend"] == "down":
            score -= 2
        
        score += sales_data["sales_last_quarter"] / 1000
        score += kpi_data["employee_efficiency"] * 2
        return {"decision_score": score, "risk": random.choice(["low", "medium", "high"])}

class StrategyGeneratorAgent:
    def generate_strategy(self, analysis_result):
        score = analysis_result["decision_score"]
        if score > 5:
            strategy = "Aggressive expansion"
        elif score > 3:
            strategy = "Moderate growth"
        else:
            strategy = "Conservative approach"
        return {"strategy": strategy, "predicted_outcome_score": score}

class DecisionReviewerAgent:
    def review(self, strategy_result):
        strategy = strategy_result["strategy"]
        predicted = strategy_result["predicted_outcome_score"]
        if predicted < 2:
            recommendation = "Delay decision, gather more data"
        else:
            recommendation = f"Approve strategy: {strategy}"
        return {"recommendation": recommendation, "confidence": predicted / 6}
