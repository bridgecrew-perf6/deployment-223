from pydantic import BaseModel
# Class which describes input feature of drug
class Drug(BaseModel):
    Age: int
    Sex: int
    BP: int
    Cholesterol: int
    Na_to_K: float

