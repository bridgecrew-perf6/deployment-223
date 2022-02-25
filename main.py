import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd
from drug import Drug
# Create the app object

app = FastAPI()
origins = [

"http://localhost",
"http://localhost:8080",
"http://localhost:3000",
]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)
# Setting up the home route

pickle_in = open("drugTree.pkl","rb")
classifier = pickle.load(pickle_in)
@app.get("/")
def read_root():
    return {"data": "Welcome to online drug  prediction model"}


# Index rout, opens automatically on localserver
"""@app.get('/')
def index():
    return {'message':'Hello I am Alive'}

# Route with a single parameter,

@app.get('/{name}')
def get_name(name: str):
    return {'message':f'Hello,{name}'}

# Expose the prediction functionality, make a prediction form pass"""


@app.post("/prediction/")
async def get_predict(data: Drug):
    data = data.dict()
    print(data)
    age = data['Age']
    sex = data['Sex']
    BP = data['BP']
    cholesterol = data['Cholesterol']
    Na_to_K = data['Na_to_K']

    prediction = classifier.predict([[age,sex,BP,cholesterol,Na_to_K]])
    if prediction=='drugX':
        prediction="Need Drug X"
    if prediction =='drugY':
        prediction = "Need Drug Y"
    else:
        prediction = "Need Drug C"
    return {

        'result':prediction

    }

# Run the API with uvicorn
if __name__=='__main__':
    uvicorn.run(app,host = '127.0.0.1',port=8080)
# uvicorn app:app --reload
