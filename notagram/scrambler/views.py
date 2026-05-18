from django.shortcuts import render
from . import anagram

def main(request):
    return testing(request)

def scrambler(request):
    return render(request, 'scrambler.html')

def testing(request):
    context = {'word': '', 'outputs': ['']}
    if request.method == 'POST':
        context['outputs'].append(anagram.scramble(request.POST['word']))
    return render(request, 'test.html', context)