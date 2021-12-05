from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('This is our projects page')

def project(request, pk):
    return HttpResponse('Single project {}'.format(str(pk)))

