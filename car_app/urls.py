from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_filtering_logs_create_view, name='car_filtering_logs'),
    #path('car_more_details/', views.next_page, name='next_page'),  


    path('ajax/load_models/', views.load_models, name='ajax_load_models'), # AJAX
    path('ajax/load_years/', views.load_years, name='ajax_load_years'), # AJAX
    path('ajax/load_engines/', views.load_engines, name='ajax_load_engines'), # AJAX
    # path('ajax/load_gearboxes/', views.load_gearboxes, name='ajax_load_gearboxes'), # AJAX
    #path('ajax/load_transmissions/', views.load_transmissions, name='ajax_load_transmissions'), # AJAX
    #path('ajax/load_bantypes/', views.load_bantypes, name='ajax_load_bantypes'), # AJAX
    #path('ajax/load_fueltypes/', views.load_fueltypes, name='ajax_load_fueltypes'), # AJAX

]