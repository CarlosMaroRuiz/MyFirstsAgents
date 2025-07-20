from pydantic import BaseModel

class ResultMath(BaseModel):
    step_operation: list[str]  
    result_final: str