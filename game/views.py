from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import GameForm
from .services import get_judgement
from .models import Question

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
            game = form
            questions = Question.objects.all()
            context = {'game': game,
                       'questions': questions,
                       'error_message': "Not all questions were answered.",
                       }
            return render(request, 'game/play.html', context)
    else:
        game = GameForm()
        questions = Question.objects.all()
        context = {'game': game, 'questions': questions}
    return render(request, 'game/play.html', context)

def results(request):
    questions = Question.objects.all()
    return render(request, 'game/results.html', {'questions': questions})
