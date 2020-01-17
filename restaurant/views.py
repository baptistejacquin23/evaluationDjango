from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.template import loader

# Create your views here.
from restaurant.forms import RestaurantForm
from restaurant.models import Restaurant


def index(request):
    template = loader.get_template("restaurants/list.html")
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return HttpResponse(template.render(context, request))


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        template = loader.get_template("restaurants/add.html")
        form = RestaurantForm()
        context = {"form": form}
        return HttpResponse(template.render(context, request))


def detail(request, pk):
    template = loader.get_template("restaurants/detail.html")
    try:
        restaurant = Restaurant.objects.get(id=pk)
    except Restaurant.DoesNotExist:
        raise Http404

    context = {"restaurant": restaurant}
    return HttpResponse(template.render(context, request))


def update(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        template = loader.get_template("restaurants/update.html")
        form = RestaurantForm(instance=restaurant)
        context = {"form": form, "restaurant": restaurant}
        return HttpResponse(template.render(context, request))
