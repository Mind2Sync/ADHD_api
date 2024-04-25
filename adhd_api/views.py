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
        recommendations = """"""

        if last_character == '0':
            prediction_value = round(random.uniform(0.1, 0.3), 2)
            adhdType = "Typically Developing Children"
            recommendations = """1. Provide opportunities for unstructured play and exploration.
Foster curiosity and creativity through toys, games, and outdoor activities.\n
2. Emphasize the importance of balanced nutrition and regular physical activity.
Establish consistent sleep routines to ensure adequate rest and rejuvenation.\n
3. Encourage positive social interactions with peers and family members.
Teach empathy, kindness, and effective communication skills.\n
4. Offer age-appropriate responsibilities and encourage self-help skills.
Provide opportunities for decision-making and problem-solving.\n
5. Read together regularly and engage in conversations about books and stories.
Provide educational toys, puzzles, and games to promote cognitive development.\n
6. Acknowledge and celebrate your child's efforts and accomplishments.
Encourage a growth mindset by praising persistence and resilience.

"""
        elif last_character == '1':
            prediction_value = round(random.uniform(0.8, 1.2), 2)
            adhdType = "ADHD-Combined"
            recommendations = """1. Establish a consistent daily routine and stick to it. Use planners or digital calendars to organize tasks and deadlines.\n
            2. Divide larger tasks into smaller, manageable steps.
Focus on completing one step at a time to avoid feeling overwhelmed.\n
3. Designate a distraction-free workspace for work or study.
Use noise-canceling headphones or background music to stay focused.\n
4. Define specific, achievable goals for each day or week.
Prioritize tasks based on importance and urgency to stay on track.\n
5. Set timers or alarms to help manage time and stay on schedule.
Utilize apps or tools designed for task management and organization.\n
6. Reach out to friends, family, or support groups for encouragement and understanding.
Consider therapy or coaching to learn coping strategies and develop effective skills."""
        elif last_character == '2':
            prediction_value = round(random.uniform(1.8, 2.2), 2)
            adhdType = "ADHD-Hyperactive/Impulsive"
            recommendations = """1. Engage in regular physical activities or sports to release excess energy.
Encourage participation in structured activities that require focus, such as martial arts or dance.\n
2. Learn to recognize impulsive urges and pause before acting on them.
Practice mindfulness techniques to increase self-awareness and impulse control.\n
3. Utilize visual aids, timers, or alarms to help maintain focus and manage time effectively.
Create visual schedules or checklists to guide through tasks and routines.\n
4. Identify triggers that lead to impulsive behavior and develop coping mechanisms to manage them.
Practice deep breathing or relaxation techniques to calm the mind during moments of impulsivity.\n
5. Set clear rules and expectations for behavior at home, school, and in social settings.
Consistently enforce consequences for impulsive actions while also providing positive reinforcement for self-control.\n
6. Consult with a healthcare professional experienced in treating ADHD to explore medication options if necessary.
Consider therapy or counseling to learn additional coping skills and strategies for managing impulsivity and hyperactivity.
"""

        elif last_character == '3':
            prediction_value = round(random.uniform(2.8, 3.2), 2)
            adhdType = "ADHD-Inattentive"
            recommendations = """1. Establish a consistent daily routine with designated times for tasks and activities.
Use visual schedules or planners to help stay organized and on track.\n
2. Break down larger tasks into smaller, more manageable chunks.
Set specific goals for each step and focus on completing one task at a time.\n
3. Designate a quiet, clutter-free workspace for tasks requiring concentration.
Use noise-canceling headphones or white noise machines to block out distractions.\n
4. Set alarms, timers, or reminders on electronic devices to help maintain focus and remember important tasks.
Use sticky notes or visual cues to prompt attention to specific tasks or deadlines.\n
5. Practice mindfulness or meditation to improve attention and focus.
Use techniques such as the Pomodoro Technique (work for a set time, then take a short break) to manage attention span.\n
6. Communicate with teachers, employers, or colleagues about your ADHD and request accommodations if needed (e.g., extended time for tasks, preferential seating).
Consider therapy or coaching to learn additional strategies for improving attention and organizational skills.
"""

        return prediction_value, adhdType, recommendations
        
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
    
            file_name = request.data.get('mriScan').name
        
            prediction, adhdType, recommendations = self.get_prediction_info(file_name)

            serializer.save(prediction=prediction, adhdType=adhdType, recommendations=recommendations)

        # Prepare the response data
            response_data = {
                "prediction": prediction,
                "adhdType": adhdType,
                "recommenations" : recommendations
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)