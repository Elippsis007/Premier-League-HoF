from django.shortcuts import render
from .models import Hof

# Create your views here.

def hof_page(request):
    """ A view to show the Hall of Famers page """

    hof = Hof.objects.all()

    context = {
        'hof': hof,
    }

    return render(request, 'hof/hof_page.html', context)