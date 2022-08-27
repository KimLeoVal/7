# from django.urls import path
#
# from webapp.views import PollView, PollDetailView, PollCreate, PollUpdate, PollDelete, ChoiceUpdate, \
#     ChoiceDelete, AnswerView, Answer, AnswerGo, ChoiceCreate1, AnswerDetailView
#
from django.urls import path

from webapp.views import ProductsView, ProductDetaillView, ProductCreate, ProductUpdate, ProductDelete, ReviewView, \
    ReviewDetaillView, ReviewCreate, ReviewUpdate, DeleteReview

app_name = 'webapp'
urlpatterns = [
    path('', ProductsView.as_view(), name='ProductsView'),
    path('product/<int:pk>', ProductDetaillView.as_view(), name='ProductDetaillView'),
#     # path('poll/<int:pk>/', PollDetailView1.as_view(), name='PollDetailView1'),
    path('create/', ProductCreate.as_view(), name='ProductCreate'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='ProductUpdate'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='ProductDelete'),
    path('review/', ReviewView.as_view(), name='ReviewView'),
    path('review/<int:pk>', ReviewDetaillView.as_view(), name='ReviewDetaillView'),
    path('review/create', ReviewCreate.as_view(), name='ReviewCreate'),
#     path('poll/<int:pk>/choice/add', ChoiceCreate1.as_view(), name='ChoiceCreate1'),
    path('review/<int:pk>/update/', ReviewUpdate.as_view(), name='ReviewUpdate'),
    path('review/<int:pk>/delete/', DeleteReview.as_view(), name='DeleteReview'),
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