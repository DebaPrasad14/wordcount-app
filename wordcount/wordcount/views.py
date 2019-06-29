from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    ourtext = request.GET['ourtext']

    wordlist = ourtext.split()


    return render(request, 'count.html', {'ourtext':ourtext, 'count':len(wordlist)})
