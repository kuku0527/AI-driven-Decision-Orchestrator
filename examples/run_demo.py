from orchestrator.orchestrator import DecisionOrchestratorAgent
import pprint

if __name__ == "__main__":
    orchestrator = DecisionOrchestratorAgent()
    result = orchestrator.run_decision_pipeline()
    pprint.pprint(result)
