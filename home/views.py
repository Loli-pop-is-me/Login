from django.shortcuts import render
from home.models import login

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['username']
        password=request.POST['password']
        print(name,password)
        print("written to db")
        ins=login(username=name,password=password)
        ins.save()
        
    var=login.objects.all()
    dicto={'content':var}
    return render (request,'index.html',dicto)