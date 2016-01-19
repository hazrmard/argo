from django.shortcuts import render
from .forms import QForm
from .helpers import *

def search_page(request):
    qform = QForm()
    results = None
    if request.method == 'GET' and 'categories' in request.GET:
        #print('printing request.GET:')
        #print(request.GET)
        qform = QForm(request.GET)
        if qform.is_valid():
            #print('Form is valid.')
            results = get_results(request.GET)
    return render(request, 'search/search.html', {'form': qform, 'results': results})
