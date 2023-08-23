import fastapi
import pickle
from pydantic import BaseModel
import uvicorn
import pandas as pd


app = fastapi.FastAPI(debug=True)


model = pickle.load(open("C:/Users/DELL PC/Desktop/Github/LP Six_ Team Qubec/LP-Six/Data/ml_model.pkl", "rb"))

@app.get('/')
def Churn(gender:str,
  Partner:str,
  Dependents:str,
  tenure:int, 
  MultipleLines:str,
  InternetService:str, 
  OnlineSecurity:str,
  OnlineBackup:str,
  DeviceProtection:str,
  TechSupport:str,
  Contract:str, 
  PaperlessBilling:str, 
  PaymentMethod:str,
  MonthlyCharges:int,
  TotalCharges:int):

  
 features = {
  'gender':gender,
  'Partner':Partner,
  'Dependents':Dependents,
  'tenure':tenure, 
  'MultipleLines':MultipleLines,
  'InternetService':InternetService, 
  'OnlineSecurity':OnlineSecurity,
  'OnlineBackup':OnlineBackup,
  'DeviceProtection':DeviceProtection,
  'TechSupport':TechSupport,
  'Contract':Contract, 
  'PaperlessBilling':PaperlessBilling, 
  'PaymentMethod':PaymentMethod,
  'MonthlyCharges':MonthlyCharges,
  'TotalCharges':TotalCharges
  }

 df = pd.DataFrame(features)

 predict = model.predict(df)

 return {'name':'customer churn'}

if __name__ == "__main__":
  uvicorn.run(app)


