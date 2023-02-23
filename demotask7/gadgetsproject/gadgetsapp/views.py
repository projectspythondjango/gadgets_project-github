from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Gadgets
from .forms import GadgetsForm

def index(request):
    gadgets=Gadgets.objects.all()

    return render(request,"index.html",{'key1':gadgets})
def detail(request,idnumber):
    gadgets1=Gadgets.objects.get(id=idnumber)
    return render(request,"detail.html",{'gadgets':gadgets1})
def addgadgets(request):
    if request.method=="POST":
        name=request.POST.get('title')
        desc1=request.POST.get('desc')
        price1=request.POST.get('price')
        img=request.FILES['image']
        gadgets1=Gadgets(title=name,desc=desc1,price=price1,image=img)
        gadgets1.save()
        return redirect('/')
    return render(request,"add.html")
def update(request,id):
    gadgets=Gadgets.objects.get(id=id)
    form1=GadgetsForm(request.POST or None,request.FILES,instance=gadgets)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form1,'gadgets':gadgets})
def delete(request,id):
    if request.method=="POST":
        gadgets=Gadgets.objects.get(id=id)
        gadgets.delete()
        return redirect('/')
    return render(request,"delete.html")


