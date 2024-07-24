from django.urls import path
from .views import MRIPredictionAPIView

urlpatterns = [
    path('', MRIPredictionAPIView.as_view(), name="Predict MRI Prediction"),
]

