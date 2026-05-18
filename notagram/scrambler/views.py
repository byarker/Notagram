from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

def main(request):
    return testing(request)

def scrambler(request):
    return render(request, 'scrambler.html')

def testing(request):
    context = {'word': '', 'prevwords': ['']}
    if request.method == 'POST':
        context['word'] = request.POST['word']
    return render(request, 'test.html', context)