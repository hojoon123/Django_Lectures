from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
# Create your views here.

def list(request):
    all_cars = models.Cars.objects.all()
    context_list =  {'all_cars' : all_cars}
    
    return render(request, 'cars/list.html', context = context_list)

def add(request):
    if request.POST:
        in_brand = request.POST['brand']
        in_year = request.POST['year']
        models.Cars.objects.create(brand = in_brand, year = in_year)
        # 사용자가 새 차를 입력했다면 리스트로 이동하세요~
        # 'cars:list' 로 가능한 이유! 
        # 앱의 urls 에서 app_name = 'cars' 해두고 list의 name이 'list' 라서 가능!
        # 이제 보니까 정말 편하네요~
        return redirect(reverse('cars:list'))
    
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.POST:
        #delete Car Number
        in_pk = request.POST['pk']
        try:
            models.Cars.objects.get(pk = in_pk).delete()
            return redirect(reverse('cars:list'))
        except:
            return render(request, 'cars/delete.html')
        
    return render(request, 'cars/delete.html')