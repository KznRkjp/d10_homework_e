from django.shortcuts import render
from carlist.models import Car, Modeltype, Manufacturer, Productionyear
from django.db.models import Q

# Create your views here.

def index(request):

    if request.method == 'GET':
        try:
            #print(58*'*')
            manufacturer_value = request.GET['manufacturer']
            #print('MAN PASS',58*'*')
            model_value = request.GET['model']
            production_year = request.GET['year']
            #year_value = request.GET['year']
            print(manufacturer_value, model_value, production_year)


            cars = Car.objects.filter(
                Q(manufacturer__id = manufacturer_value)&
                Q(models_type__id = model_value)&
                Q(production_year__id = production_year))

        #k = request.GET['man']
        except Exception as e:
            print('exception')
            print(e)
            cars = Car.objects.all()
    else:
        cars = Car.objects.all()


    man_list = Manufacturer.objects.all()
    model_list = Modeltype.objects.all()
    year_list = Productionyear.objects.all()
    return render(request, 'carlist/index.html', {'cars':cars, 'manufacturers':man_list, 'models':model_list, 'years':year_list})



    # # def get_options(name):
    # #     option_query = Car.objects.values(name).distinct()
    # #     option_list = []
    # #     for i in option_query:
    # #         option_list.append(i[name])
    # #     return sorted(option_list)
    #
    # def check_get(request, name):
    #     try:
    #         result = request.GET[name]
    #         if result == '--':
    #             result = 'All'
    #     except():
    #         result = 'All'
    #     return result
