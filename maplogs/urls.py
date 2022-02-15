from django.urls import path
from . import views

app_name = 'maps'

handler404 = 'maplogs.views.page_not_found'
urlpatterns = [
    path('', views.map_list, name='map_list'),
    path('search', views.search, name='search'),
    path('details/<int:map_id>', views.map_details, name='map_details'),
    path('filter/rims', views.map_filter_rim, name='map_filter_rim'),
    path('filter/pdp', views.map_filter_pdp, name='map_filter_pdp'),
    path('filter/cadastral', views.map_filter_cadastral, name='map_filter_cadastral'),
    path('filter/county', views.filter_by_county, name='filter_by_county'),
    path('getmap/<int:map_id>/', views.get_map, name='get_map'),
]
