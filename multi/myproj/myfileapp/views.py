from django.shortcuts import render, HttpResponse
# Create your views here.
from . models import myuploadfile

def index(request):
    documents = myuploadfile.objects.all()
    return render(request, "index.html", context={
        "files": documents
    })

def send_files(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        for f in myfile:
            myuploadfile(f_name=name, myfiles=f).save()

        return HttpResponse("ok")