from django.shortcuts import render

# Create your views here.

def hof(request):
    """ A view to show the Hall of Famers page """

    return render(request, 'hof/hof.html')