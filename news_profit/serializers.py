from rest_framework import serializers
from .models import User, FavoriteNews
from news_profit.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id username'.split()


class FavoriteNewsSerializer(serializers.ModelSerializer):
    user = UserSerializer
    news = NewsSerializer

    class Meta:
        model = FavoriteNews
        fields = 'id user news'.split()