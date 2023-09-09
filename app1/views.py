from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.
def student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('not valid')
    return render(request,'student.html',d)