from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
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
    user = request.user.is_authenticated
    if user:
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
    else:
        raise Http404


def detail(request, pk):
    template = loader.get_template("restaurants/detail.html")
    try:
        restaurant = Restaurant.objects.get(id=pk)
    except Restaurant.DoesNotExist:
        raise Http404

    context = {"restaurant": restaurant}
    return HttpResponse(template.render(context, request))


def update(request, pk):
    user = request.user.is_authenticated
    if user:
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
    else:
        raise Http404


def delete(request, pk):
    user = request.user.is_authenticated
    if user:
        restaurant_to_delete = get_object_or_404(Restaurant, id=pk)
        restaurant_to_delete.delete()
        return redirect('index')
    else:
        raise Http404
