from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MRIPrediction
from .serializers import MRIPredictionSerializer
# from .adhdPredict import predictAdhd  # Assuming you have adhdPredict.py
import os

# class MRIPredictionAPIView(APIView):
#     serializer_class = PredictionSerializerPost

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # Extract data from request
#             name = serializer.validated_data.get("name")
#             age = serializer.validated_data.get("age")
#             sex = serializer.validated_data.get("sex")
#             country = serializer.validated_data.get("country")
#             mri_scan = request.FILES.get("mriScan")  # Retrieve .nii file

#             # Perform prediction
#             prediction = predictAdhd(mri_scan)

#             # Save prediction to database
#             serializer.save(prediction=prediction)

#             # Prepare response data
#             response_data = {
#                 "prediction": prediction,
#             }
#             return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MRIPredictionAPIView(APIView):
    serializer_class = MRIPredictionSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Assigning a constant default prediction value for testing
            prediction_value = 0.75

            # Save the constant prediction value to the database
            serializer.save(prediction=prediction_value)

            # Prepare the response data
            response_data = {
                "prediction": prediction_value,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
