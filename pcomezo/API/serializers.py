from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from . import models


class TagSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = (
            'name',
            'type'
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answers
        fields = (
            'id',
            'question',
            'a_text',
            'correct',
        )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source="related_question", many=True, read_only=True)
    created_by_name = serializers.ReadOnlyField(source='created_by.username')
    tags_desc = TagSerializer(source="tags", many=True, queryset=models.Tags.objects.all())

    class Meta:
        model = models.Questions
        fields = (
            'id',
            'created_by',
            'created_by_name',
            'created_at',
            'q_text',
            'tags_desc',
            'hint',
            'answers'
        )


class SearchSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = models.Questions
        fields = (
            '__all__'
        )
