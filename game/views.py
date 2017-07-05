from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import GameForm
from .services import get_judgement
#from .models import Question

def home(request):
    return render(request, 'game/home.html', {})

def play(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            judge = get_judgement(form_data)
            messages.add_message(request, messages.INFO, judge)
            return redirect('game:results')
    else:
        game = GameForm()
    return render(request, 'game/play.html', {'game': game})

def results(request):
    #questions = Question.objects.all()
    #return render(request, 'game/results.html', {'questions': questions})
    questions = "Questions"
    return render(request, 'game/results.html', {'questions': questions})
