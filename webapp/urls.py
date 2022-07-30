from django.urls import path

from webapp.views import PollView, PollDetailView, PollCreate, PollUpdate, PollDelete, ChoiceUpdate, \
    ChoiceDelete, AnswerView, Answer, AnswerGo, ChoiceCreate1
urlpatterns = [
    path('', PollView.as_view(), name='PollView'),
    path('poll/<int:pk>', PollDetailView.as_view(), name='PollDetailView'),
    # path('poll/<int:pk>/', PollDetailView1.as_view(), name='PollDetailView1'),
    path('create/', PollCreate.as_view(), name='PollCreate'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(), name='PollUpdate'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='PollDelete'),
    path('poll/<int:pk>/choice/add', ChoiceCreate1.as_view(), name='ChoiceCreate1'),
    path('choice/<int:pk>/update/', ChoiceUpdate.as_view(), name='ChoiceUpdate'),
    path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name='ChoiceDelete'),
    path('answer/', AnswerView.as_view(), name='AnswerView'),
    path('answer/<int:pk>', AnswerGo.as_view(), name='AnswerGo'),






]