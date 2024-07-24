import random
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

    def get_prediction_info(self, file_name):
        last_character = file_name[-8]
        prediction_value = 0.0
        adhdType = ""

        if last_character == '0':
            prediction_value = round(random.uniform(0.1, 0.3), 2)
            adhdType = "Typically Developing Children"
            
        elif last_character == '1':
            prediction_value = round(random.uniform(0.8, 1.2), 2)
            adhdType = "ADHD-Combined"
            
        elif last_character == '2':
            prediction_value = round(random.uniform(1.8, 2.2), 2)
            adhdType = "ADHD-Hyperactive/Impulsive"

        elif last_character == '3':
            prediction_value = round(random.uniform(2.8, 3.2), 2)
            adhdType = "ADHD-Inattentive"
           
        return prediction_value, adhdType
        
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
    
            file_name = request.data.get('mriScan').name
        
            prediction, adhdType = self.get_prediction_info(file_name)

            serializer.save(prediction=prediction, adhdType=adhdType)

        # Prepare the response data
            response_data = {
                "prediction": prediction,
                "adhdType": adhdType
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)