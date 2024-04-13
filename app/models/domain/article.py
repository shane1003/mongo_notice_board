from pydantic import BaseModel
from typing import List
from datetime import datetime as dt

class article(BaseModel):
    title : str
    no : int
    user_id : str
    content : str
    views : int
    date : dt