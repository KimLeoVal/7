
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll, Choice, Answer


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

# class PollDetailView1(DetailView):
#     model = Poll
#     template_name = 'for_poll/view1.html'
#     context_object_name = 'poll'

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

class ChoiceCreate1(CreateView):
    template_name = 'for_choice/create.html'
    form_class = ChoiceForm


    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        form.instance.poll = poll
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


class AnswerView(ListView):
    model = Answer
    template_name = 'for_answer/index_answer.html'
    context_object_name = 'answer'

class AnswerDetailView(DetailView):
    model = Answer
    template_name = 'for_answer/view.html'
    context_object_name = 'answer'

class AnswerGo(TemplateView):
    template_name = 'for_answer/answer.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer = get_object_or_404(Answer, pk=kwargs['pk'])
        print(answer.poll_id)
        choice = Choice.objects.filter(poll__id=answer.poll_id)
        print(choice)
        context['answer'] = answer
        context['choice'] = choice
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        answer = get_object_or_404(Answer, pk=pk)
        choice_id = request.POST.get('answer')
        # choices = Choice.objects.filter(poll__id=answer.poll_id)
        # choice_id =
        # choice_id=Choice.objects.get(pk=choice_id)
        # poll_id = kwargs['pk']
        # poll_id = Poll.objects.get(pk = poll_id)
        answer.choice_id=choice_id
        # answer.poll_id=pk
        print(answer)
            # Answer.objects.create(choice_id=choice_id, poll_id=pk)
        answer.save()
        return redirect('AnswerDetailView', pk=answer.pk)








