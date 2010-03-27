from django.shortcuts import render_to_response
from django.http import HttpResponse
from erp.product.models import *

def search(request):
    return render_to_response('searchform.html')

def search_form(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        p = product.objects.filter(name__icontains=q)
        return render_to_response('search_results.html',
            {'products': p, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
