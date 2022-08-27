# from django.urls import path
#
# from webapp.views import PollView, PollDetailView, PollCreate, PollUpdate, PollDelete, ChoiceUpdate, \
#     ChoiceDelete, AnswerView, Answer, AnswerGo, ChoiceCreate1, AnswerDetailView
#
from django.urls import path

from webapp.views import ProductsView, ProductDetaillView, ProductCreate, ProductUpdate, ProductDelete

app_name = 'webapp'
urlpatterns = [
    path('', ProductsView.as_view(), name='ProductsView'),
    path('product/<int:pk>', ProductDetaillView.as_view(), name='ProductDetaillView'),
#     # path('poll/<int:pk>/', PollDetailView1.as_view(), name='PollDetailView1'),
    path('create/', ProductCreate.as_view(), name='ProductCreate'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='ProductUpdate'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='ProductDelete'),
#     path('poll/<int:pk>/choice/add', ChoiceCreate1.as_view(), name='ChoiceCreate1'),
#     path('choice/<int:pk>/update/', ChoiceUpdate.as_view(), name='ChoiceUpdate'),
#     path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name='ChoiceDelete'),
#     path('answer/', AnswerView.as_view(), name='AnswerView'),
#     path('answer/<int:pk>', AnswerGo.as_view(), name='AnswerGo'),
#     path('answer/<int:pk>/detail', AnswerDetailView.as_view(), name='AnswerDetailView'),
#
#
#
#
#
#
#
]