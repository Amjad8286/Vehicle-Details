from django.shortcuts import render, redirect
from .models import VehiclesDetail

# Create your views here.
def Index(request):
    vehicles = VehiclesDetail.objects.all().order_by('-v_id')
    
    return render(request, 'table.html',{'vehicles': vehicles})

def Create(request):
    if request.method == "POST":
        engine_status = request.POST.get('engine_status')
        fuel_level = request.POST.get('fuel_level')
        tampreture = request.POST.get('tampreture')
        average_speed = request.POST.get('average_speed')
        speed = request.POST.get('speed')
        vehicles = VehiclesDetail(engine_status=engine_status, fuel_level=fuel_level, 
                                  tampreture=tampreture, average_speed=average_speed, speed=speed)
        vehicles.save()
        return redirect('home')

    return render (request, 'form.html')

def Update(request, no):
    vehicles= VehiclesDetail.objects.get(v_id=no)
    if request.method == "POST":
        Id = request.POST.get('id')
        engine_status = request.POST.get('engine_status')
        fuel_level = request.POST.get('fuel_level')
        tampreture = request.POST.get('tampreture')
        average_speed = request.POST.get('average_speed')
        speed = request.POST.get('speed')
        vehicles = VehiclesDetail(v_id=Id, engine_status=engine_status, fuel_level=fuel_level, 
                                  tampreture=tampreture, average_speed=average_speed, speed=speed)
        vehicles.save()
        return redirect('home')

    return render(request, 'update.html', {'vehicles':vehicles})

def Delete(request, no):
        vehicles = VehiclesDetail.objects.get(v_id=no)
        vehicles.delete()
        return redirect ('home')

