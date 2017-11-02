from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from .models import Questions, Answers
from .serializers import QuestionSerializer, AnswerSerializer, SearchSerializer


class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return self.queryset.filter(question_id=self.kwargs.get("question_pk"))

    def perform_create(self, serializer):
        question = get_object_or_404(Questions, pk=self.kwargs.get('question_pk'))
        serializer.save(question=question)


class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            question_id=self.kwargs.get('question_pk'),
            pk=self.kwargs.get('pk')
        )


class SearchView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = SearchSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(tags__name__icontains=query) |
                Q(q_text__icontains=query)
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
