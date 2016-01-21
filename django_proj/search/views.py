from django.shortcuts import render
from .forms import QForm
from .helpers import *

def search_page(request):
    qform = QForm()
    results = None
    url = ''
    if request.method == 'GET' and 'categories' in request.GET:
        qform = QForm(request.GET)
        if qform.is_valid():
            results, url = get_results(dict(request.GET))
    return render(request, 'search/search.html', {'form': qform, 'results': results, 'url': url})
