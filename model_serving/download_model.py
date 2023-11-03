import mlflow
import pickle

model_name = 'teste-svm'
stage = 'Production'
model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")
print('oi')
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
