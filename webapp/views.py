from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll, Choice


class PollView(ListView):
    model = Poll
    template_name = 'for_poll/index.html'
    context_object_name = 'poll'
    paginate_by = 5
    ordering = '-created_ad'

class PollDetailView(DetailView):
    model = Poll
    template_name = 'for_poll/view.html'
    context_object_name = 'poll'

class PollCreate(CreateView):
    template_name = 'for_poll/create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('PollDetailView', kwargs={'pk': self.object.pk})

class PollUpdate(UpdateView):
    template_name = 'for_poll/update.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('PollDetailView', kwargs={'pk': self.object.pk})

class PollDelete(DeleteView):
    model = Poll
    context_object_name = 'poll'
    template_name = 'for_poll/delete.html'
    success_url = reverse_lazy('PollView')

class ChoiceView(ListView):
    model = Choice
    template_name = 'for_poll/view.html'
    context_object_name = 'choice'

class ChoiceCreate(CreateView):
    template_name = 'for_choice/create.html'
    form_class = ChoiceForm


    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.choice = poll
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('PollDetailView', kwargs={'pk': self.object.poll.pk})

class ChoiceUpdate(UpdateView):
    template_name = 'for_choice/update.html'
    model = Choice
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('PollDetailView', kwargs={'pk': self.object.poll.pk})

class ChoiceDelete(DeleteView):
    model = Choice
    context_object_name = 'choice'
    template_name = 'for_choice/delete.html'
    success_url = reverse_lazy('PollView')



