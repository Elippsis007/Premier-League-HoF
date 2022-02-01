from django.shortcuts import render

# Create your views here.

def hof_page(request):
    """ A view to show the Hall of Famers page """

    return render(request, 'hof/hof_page.html')