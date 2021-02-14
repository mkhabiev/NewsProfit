from django.urls import path
from . import views as consultant

urlpatterns = [
    path('api/v1/consult/', consultant.QuestionAPIView.as_view()),
]