from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    ourtext = request.GET['ourtext']

    wordlist = ourtext.split()
    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1    # if word already present then increse count
        else:
            word_dict[word] = 1     # if word not present then initialize count to 1

    sortedWords = sorted(word_dict.items(), key= operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'ourtext':ourtext, 'count':len(wordlist), 'sortedWords':sortedWords})
