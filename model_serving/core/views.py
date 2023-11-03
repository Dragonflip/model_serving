from rest_framework.views import APIView
from rest_framework.response import Response
from .apps import CoreConfig


class Prediction(APIView):
    def post(self, request):
        sepal_length = request.data.get('sepal_length')
        sepal_width = request.data.get('sepal_width')
        petal_length = request.data.get('petal_length')
        petal_width = request.data.get('petal_width')

        model = CoreConfig.model
        predict_values = {
                'sepal_length': float(sepal_length),
                'sepal_width': float(sepal_width),
                'petal_length': float(petal_length),
                'petal_width': float(petal_width),
        }
        prediction = model.predict(predict_values)
        response_dict = {
                'predicted class': prediction
        }
        return Response(response_dict, status=200)

