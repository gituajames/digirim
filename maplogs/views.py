# from django import template
from django.http.response import Http404
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
# import datetime

from . models import Map
from .forms import GetMapForm
from django.core.mail import send_mail

# to do
'''
    display all available maps and make queries and the scanned status and dates
    create maps orders or requests and download for scanned maps
    if map is hardcopy request a print in advance i.e send a request(text/email) to the printing people

    and make payments

    admin
    add maps scanned and soft copies
'''

from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'maps/404.html', {})


def map_list(request):
    maps = Map.objects.all()
    return render(request, 'maps/map_list.html', {'maps': maps})


def map_filter_rim(request):
    maps = Map.objects.filter(map_category='General Boundary')
    return render(request, 'maps/map_list.html', {'maps': maps})


def map_filter_pdp(request):
    maps = Map.objects.filter(map_category='PDP')
    return render(request, 'maps/map_list.html', {'maps': maps})


def map_filter_cadastral(request):
    maps = Map.objects.filter(map_category='Cadastral')
    return render(request, 'maps/map_list.html', {'maps': maps})


def filter_by_county(request):
    """filter by county names"""
    try:
        maps = Map.objects.filter(county__icontains=request.GET.get('county'))
        return render(request, 'maps/map_list.html', {'maps': maps})
    except Map.DoesNotExist:
        raise Http404('404 no such county')


def search(request):
    """search title of maps by any name"""
    print(request.GET.get('search'))
    query = request.GET.get('search')
    
    try:
        maps = Map.objects.filter(title__icontains=query)
    except Map.DoesNotExist:
        raise Http404('404 map not available')
        # return render(request, 'maps/map_list.html', {'maps': maps})
    
    context = {
        'maps': maps
    }

    return render(request, 'maps/map_list.html', context)


def map_details(requests, map_id):
    
    try:
        maps = Map.objects.get(pk=map_id)
    except Map.DoesNotExist:
        # raise Http404('404 you seem lost')
        return render(requests, 'maps/404.html', {'map_id': map_id})
    context = {

        'map': maps
        
    }
    return render(requests, 'maps/map_detail.html', context)


def get_map(request, map_id):
    map_sent = False

    if request.method == 'POST':
        form = GetMapForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            map_ = Map.objects.get(pk=map_id)
            subject = f"{map_.title}"
            message = f"find the attached map {map_.title}"
            send_mail(subject, message, 'info@geomird.co.ke', [cd['email']])

            map_sent = True

    else:
        form = GetMapForm()
    return render(request, 'maps/get_map.html', {'form': form,
                                                 'map_sent': map_sent})
