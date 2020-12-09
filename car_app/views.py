
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import car_filtering_logsCreationForm
from .models import Car,MarkaModel, ModelYear, YearEngine, EngineGearbox, GearboxTransmission, TransmissionBantype, BantypeFueltype,car_filtering_logs, car_information, car_information_details

from django.template import RequestContext
import pdb

def car_filtering_logs_create_view(request):
    form = car_filtering_logsCreationForm()
    if request.method == 'POST':
        form = car_filtering_logsCreationForm(request.POST)

        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('car_filtering_logs')

        else:
            print("it is not valid")
            #print(form['engine'].value())
            print(form.errors)
    return render(request, 'home.html', {'form': form})



# AJAX
def load_models(request):
    # pdb.set_trace()
    marka_id = request.GET.get('marka_id')

    # models = MarkaModel.objects.filter(marka=marka_id)
    models = Car.objects.filter(marka=marka_id)

    print(models[0]['id'])
    print(models[0]['model'])
    return render(request, 'car_app/model_dropdown_list_options.html', {'models': models})


# AJAX
def load_years(request):
    marka_id = request.GET.get('marka_id')
    model_id = request.GET.get('model_id')

    years = ModelYear.objects.filter(marka=marka_id, model=model_id).order_by('year')
    #print(years)
    return render(request, 'car_app/year_dropdown_list_options.html', {'years': years})

# AJAX
def load_engines(request):
    marka_id = request.GET.get('marka_id')
    model_id = request.GET.get('model_id')
    year_id = request.GET.get('year_id')

    engines = YearEngine.objects.filter(marka=marka_id, model=model_id, year=year_id).order_by('engine')
    #print(engines)
    return render(request, 'car_app/engine_dropdown_list_options.html', {'engines': engines})


# # AJAX
# def load_gearboxes(request):
#     marka_id = request.GET.get('marka_id')
#     model_id = request.GET.get('model_id')
#     year_id = request.GET.get('year_id')
#     engine_id = request.GET.get('engine_id')
#     print("marka id is : {}".format(marka_id))
#     print("model id is : {}".format(model_id))
#     print("year id is : {}".format(year_id))
#     print("engine is equal : {}".format(engine_id))
#     gearboxes = EngineGearbox.objects.filter(marka=marka_id, model=model_id, year=year_id, engine=engine_id).distinct('gearbox')
#     print(gearboxes)
#     #print(list(years.values('id', 'year','model_id')))
#     return render(request, 'car_app/gearbox_dropdown_list_options.html', {'gearboxes': gearboxes})
#     #return JsonResponse(list(years.values('id', 'year')), safe=False) 


# # AJAX
# def load_transmissions(request):
#     marka_id = request.GET.get('marka_id')
#     model_id = request.GET.get('model_id')
#     year_id = request.GET.get('year_id')
#     engine_id = request.GET.get('engine_id')
#     gearbox_id = request.GET.get('gearbox_id')
#     print("marka id is : {}".format(marka_id))
#     print("model id is : {}".format(model_id))
#     print("year id is : {}".format(year_id))
#     print("engine is equal : {}".format(engine_id))
#     print(gearbox_id)
#     transmissions = GearboxTransmission.objects.filter(marka=marka_id, model=model_id, year=year_id, engine=engine_id, gearbox=gearbox_id).distinct('transmission')
#     print(transmissions)
#     #print(list(years.values('id', 'year','model_id')))
#     return render(request, 'car_app/transmission_dropdown_list_options.html', {'transmissions': transmissions})
#     #return JsonResponse(list(years.values('id', 'year')), safe=False) 


# # AJAX
# def load_bantypes(request):
#     marka_id = request.GET.get('marka_id')
#     model_id = request.GET.get('model_id')
#     year_id = request.GET.get('year_id')
#     engine_id = request.GET.get('engine_id')
#     gearbox_id = request.GET.get('gearbox_id')
#     transmission_id = request.GET.get('transmission_id')
#     print("pppppppppppp")
#     print("transmission is {}".format(transmission_id))
#     bantypes = TransmissionBantype.objects.filter(marka=marka_id, model=model_id, year=year_id, engine=engine_id, gearbox=gearbox_id, transmission=transmission_id).distinct('ban_type')
#     print(bantypes)
#     #print(list(years.values('id', 'year','model_id')))
#     return render(request, 'car_app/bantype_dropdown_list_options.html', {'bantypes': bantypes})
#     #return JsonResponse(list(years.values('id', 'year')), safe=False) 


# # AJAX
# def load_fueltypes(request):
#     print("popopo")
#     marka_id = request.GET.get('marka_id')
#     model_id = request.GET.get('model_id')
#     year_id = request.GET.get('year_id')
#     engine_id = request.GET.get('engine_id')
#     gearbox_id = request.GET.get('gearbox_id')
#     transmission_id = request.GET.get('transmission_id')
#     bantype_id = request.GET.get('ban_type_id')
#     print("llllllllllllllllllllllllllllllll")
#     print(bantype_id)
#     fueltypes = BantypeFueltype.objects.filter(marka=marka_id, model=model_id, year=year_id, engine=engine_id, gearbox=gearbox_id, transmission=transmission_id, ban_type=bantype_id).distinct('fuel_type')
#     print(fueltypes)
#     #print(list(years.values('id', 'year','model_id')))
#     return render(request, 'car_app/fueltype_dropdown_list_options.html', {'fueltypes': fueltypes})
#     #return JsonResponse(list(years.values('id', 'year')), safe=False) 


# def next_page(request):
#     #m_id =  request.POST.get('id')
    
#     #patient = get_object_or_404(buying_cars, pk=buying_car_id)
#     #print(patient)
#     form = car_informationCreationForm()
#     if request.method == 'POST':
#         form = car_informationCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #return redirect('buying_cars_details')
#     #return HttpResponse('We have recieved your car information...we will call you!')
#     m_id = car_information.objects.latest('id')
#     print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#     print(m_id.id)
#     form = car_information_detailsCreationForm()
#     if request.method == 'POST':
#         form = car_information_detailsCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

#     return render(request, 'details.html', {'form': form})
    