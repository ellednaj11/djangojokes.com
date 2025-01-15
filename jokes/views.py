from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Joke
class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy("jokes:list")
