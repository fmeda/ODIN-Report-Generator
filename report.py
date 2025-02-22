from pydantic import BaseModel
from typing import List

class Report(BaseModel):
    hostids: List[int]
    time_from: str
    time_till: str
    format: str
    output_dir: str
