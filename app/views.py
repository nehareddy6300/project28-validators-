from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *

# Create your views here.
def Create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sl=SFDO.cleaned_data['slocation']
            sp=SFDO.cleaned_data['sprincipal']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['renteremail']

            NSDO=School.objects.get_or_create(sname=sn,slocation=sl,sprincipal=sp,email=e,renteremail=re)[0]
            NSDO.save()

            return HttpResponse('school is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_school.html',d)
                            


    
