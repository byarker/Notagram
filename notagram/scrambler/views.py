from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

'''
def main(request):
  template = loader.get_template('scrambler.html')
  return HttpResponse(template.render())
'''
def main(request):
    return testing(request)

def scrambler(request):
    return render(request, 'scrambler.html')

def testing(request):
  return render(request, 'test.html')