from django.http import HttpResponse
from django.template import loader

# Create your views here.
from restaurant.models import Restaurant


def index(request):
    template = loader.get_template("restaurants/list.html")
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return HttpResponse(template.render(context, request))
