from django.forms import SlugField
from django.shortcuts import render
from .models import Reports
from .forms import apply_form
# Create your views here.
def list(request):
    list = Reports.objects.all()
    
    return render(request,'job_list.html',{'list':list})

def details(request,slug):
    detail = Reports.objects.get(slug=slug)
    if request.method == 'POST':
        form = apply_form(request.POST,request.FILES)
        if form.is_valid:
            my_form = form.save(commit=False)
            my_form.titl = detail
            my_form.save()
           
            
            
    else :
        form = apply_form()
        
    context = {'detail':detail,'form':form}
    return render(request,'job_details.html',context)

   