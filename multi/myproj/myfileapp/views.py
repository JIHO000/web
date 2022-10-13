from django.shortcuts import render, HttpResponse
# Create your views here.
from . models import myuploadfile
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    documents = myuploadfile.objects.order_by('id')
    paginator = Paginator(documents, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    return render(request, "index.html", context={
        'question_list': page_obj
    })

def send_files(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        for f in myfile:
            myuploadfile(f_name=name, myfiles=f).save()

        return HttpResponse("ok")