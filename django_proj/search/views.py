from django.shortcuts import render
from .forms import QueryForm, QForm

def search_page(request):
    form = QueryForm()
    qform = QForm()
    if request.method == 'GET':
        print(request.GET)
    return render(request, 'search/search.html', {'form': qform})
