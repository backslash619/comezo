from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.QuestionListCreateAPIView.as_view(), name="question_list"),
    url(r'^(?P<pk>\d+)/$', views.QuestionRetrieveUpdateDestroyAPIView.as_view(), name="question_detail"),
    url(r'^(?P<question_pk>\d+)/answers/$',
        views.AnswerListCreateAPIView.as_view(), name="answer_list"),
    url(r'^(?P<question_pk>\d+)/answers/(?P<pk>\d+)$',
        views.AnswerRetrieveUpdateDestroyAPIView.as_view(), name="answer_detail"),

    url(r'^search/$',views.SearchView.as_view())
]
