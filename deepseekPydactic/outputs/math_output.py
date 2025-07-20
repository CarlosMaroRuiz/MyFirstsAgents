from pydantic import BaseModel

class StatisticsResult(BaseModel):
    analysis_steps: list[str]
    final_conclusion: str
    latex_code: str

    details_execution: str