from django.urls import path
from . import views as news_profit

urlpatterns = [
    path('api/v1/news/', news_profit.NewsAPIView.as_view()),
    path('api/v1/news/<int:id>/', news_profit.NewsAPIViewDetail.as_view()),
    path('api/v1/register/', news_profit.RegisterApiView.as_view()),
    path('api/v1/confirm/', news_profit.ConfirmApiView.as_view()),
    path('api/v1/login/', news_profit.LoginApiView.as_view()),
]