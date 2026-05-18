from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

'''
def main(request):
  template = loader.get_template('scrambler.html')
  return HttpResponse(template.render())
'''
def main(request):
    return scrambler(request)

def scrambler(request):
    return render(request, 'scrambler.html')

def testing(request):
  template = loader.get_template('test.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))