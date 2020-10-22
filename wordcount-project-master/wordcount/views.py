from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')
    # return render(request, 'home.html', {'HiKanu': "This is me"})


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # increase the count
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1
    sorted_words = sorted(word_dictionary.items(),
                          key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {'fulltext': fulltext, "count": len(word_list), 'word_dictionary': sorted_words})


def about(request):
    return render(request, "about.html")

# def eggs(request):
#     return HttpResponse("<h1>Eggs are great</h1> and I eat every day")
