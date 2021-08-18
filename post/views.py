from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
import django
import models
import pwden
from django.http import JsonResponse
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def choise_car_brand(request):
    if request.method == 'POST':
        pass
    else:
        try:
            car_brand_list = models.car.objects.all().values('car_brand').distinct()
        except Exception:
            return render(request, 'choise_car_brand.html', {'login_err': 'loadcar_brandfail'})
        return render(request, 'choise_car_brand.html', {'car_brand_list': car_brand_list})


def pick_up_car_model(request):
    if request.method == 'GET':
        car_brand = request.GET.get('car_brand')
        if car_brand:
            data = list(models.car.objects.filter(
                car_brand=car_brand).values('car_model'))
            return JsonResponse(data, safe=False)
