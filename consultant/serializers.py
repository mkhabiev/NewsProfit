from rest_framework import serializers
from consultant.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = 'id text answers'.split()
        comments = serializers.SerializerMethodField()

        def get_answer(self, obj):
            answers = Answer.objects.filter(question=obj)
            return AnswerSerializer(answers, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = 'id text'.split()