from django.urls import path

from webapp.views import PollView, PollDetailView, PollCreate, PollUpdate, PollDelete, ChoiceCreate, ChoiceUpdate, \
    ChoiceDelete

urlpatterns = [
    path('', PollView.as_view(), name='PollView'),
    path('poll/<int:pk>', PollDetailView.as_view(), name='PollDetailView'),
    path('create/', PollCreate.as_view(), name='PollCreate'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(), name='PollUpdate'),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='PollDelete'),
    # path('projects/', ProjectView.as_view(), name='ProjectView'),
    # path('projects/<int:pk>', DetailProjectView.as_view(), name='DetailProjectView'),
    # path('choice/create', ChoiceCreate.as_view(), name='ChoiceCreate'),
    path('poll/<int:pk>/choice/add', ChoiceCreate.as_view(), name='ChoiceCreate'),
    path('choice/<int:pk>/update/', ChoiceUpdate.as_view(), name='ChoiceUpdate'),
    path('choice/<int:pk>/delete/', ChoiceDelete.as_view(), name='ChoiceDelete'),
    # path('projects/<int:pk>/softdelete/', SoftDeleteProject.as_view(), name='SoftDeleteProject'),





]