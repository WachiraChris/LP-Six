# Deploying Machine Learning Models using FastAPI: A CRISP-DM Framework Approach  

In the rapidly evolving landscape of data science and machine learning, deploying models into real-world applications is a crucial step to turn insights into tangible value. FastAPI, a modern web framework for building APIs with Python, provides an efficient and user-friendly way to deploy machine learning models. 
In this article, we'll walk through the deployment process using FastAPI while adhering to the CRISP-DM (Cross-Industry Standard Process for Data Mining) framework, a widely recognized methodology for data science projects.  

## Understanding the CRISP-DM Framework
CRISP-DM consists of six major phases, providing a structured approach to guide data science projects:

- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment  
Each phase builds upon the insights gained from the previous ones, fostering a well-organized and iterative workflow. While deploying a machine learning model, we'll integrate these phases into the FastAPI development process.

### Phase 1: Business Understanding
we will be using the [sepsis](https://www.kaggle.com/datasets/chaunguynnghunh/sepsis) dataset from kaggle.com, and our aim is to develop a machine learning model that will be able to predict with high accuracy if a patient in the ICU will develop sepsis or not and also deploy the model using FastAPI.

### Phase 2: Data Understanding
The dataset for this project is already available on Kaggle, and the following columns and brief descriptions about them are available:
1. ID	N/A	Unique number to represent patient ID
2. PRG	Attribute1	Plasma glucose
3. PL	Attribute 2	Blood Work Result-1 (mu U/ml)
4. PR	Attribute 3	Blood Pressure (mm Hg)
5. SK	Attribute 4	Blood Work Result-2 (mm)
6. TS	Attribute 5	Blood Work Result-3 (mu U/ml)
7. M11	Attribute 6	Body mass index (weight in kg)/(height in m)^2
8. BD2	Attribute 7	Blood Work Result-4 (mu U/ml)
9. Age	Attribute 8	patients age (years)
10. Insurance	N/A	If a patient holds a valid insurance card
11. Sepssis	Target	Positive: if a patient in ICU will develop a sepsis, and Negative: otherwise

### Phase 3: Data Preparation
We did some analysis on the dataset, including Exploratory data analysis, Univariate, Bivariate and Multivariate analysis. The notebook for the analysis can be found [here]()
### Phase 4: Modeling
Train your machine learning model using the prepared data. Once the model is trained, save it in a format that can be loaded during deployment. Commonly, this is done using joblib or pickle.
### Phase 5: Evaluation
We trained and evaluated 7 models to be able to select the best model, again, the details can be found in this [notebook]().
### Phase 6: Deployment
Now, let's delve into the deployment process using FastAPI:

  - Step 1: Set Up Your Environment
     Before you begin, make sure you have Python 3.7 or later version installed. 
     You can create a virtual environment to isolate your project dependencies:
     ```python
      python -m venv myenv
      ./myenv/Scripts/activate
      ```
  - Step 2: Install Dependencies
     FastAPI and Uvicorn (ASGI server) are the main dependencies you'll need for this project:
      ```python
      pip install fastapi uvicorn
      ```
    Additionally, you might require other libraries depending on your machine learning model and data processing requirements.

  - Step 3: Build Your Machine Learning Model
     Create and train your machine learning model using libraries like Scikit-learn, TensorFlow, or PyTorch. Save the trained model to disk using serialization techniques like pickle or the model's built-in methods.

  - Step 4: Create a FastAPI App
    Create a new Python file (e.g., main.py) and define your FastAPI app:

    ```
    from fastapi import FastAPI

    app = FastAPI()
   ```
# Import your trained machine learning model here
# For example: from my_ml_model import MyModel
Step 5: Define API Endpoints
Define the endpoints that your app will expose. These endpoints will be used to interact with your machine-learning model. For instance:

```python

@app.post("/predict/")
async def predict(data: dict):
    # Use your machine learning model to make predictions
    # For example: result = MyModel.predict(data)
    return {"prediction": result}
```

Step 6: Run the App Locally
You can now run your FastAPI app locally for testing:


uvicorn main:app --host 0.0.0.0 --port 8000
Visit http://127.0.0.1:8000/docs in your browser to access the automatically generated Swagger documentation and interact with your API.

Step 7: Deploy to Production
To deploy your FastAPI app in a production environment, you'll need a production-ready ASGI server like Gunicorn or Hypercorn. Install the server of your choice and start the app:
```python
  pip install gunicorn
  gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```
Make sure to configure a reverse proxy (e.g., Nginx) to handle incoming requests and forward them to the Gunicorn server.

## Conclusion
Deploying machine learning applications can be a complex task, but with tools like FastAPI, the process becomes more manageable and efficient. FastAPI's simplicity, automatic documentation generation, and performance make it an excellent choice for building APIs to deploy your machine learning models. By following the steps outlined in this guide, you can create, deploy, and serve your machine learning app to users, enabling them to interact with your models and benefit from your data-driven insights.
