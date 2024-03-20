from pydantic import BaseModel


class AnalyseLogsSchema(BaseModel):
    input: str
