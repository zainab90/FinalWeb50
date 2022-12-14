from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from serviceApp.forms import CategoryForm, ServiceForm
from serviceApp.models import Category, Service, SlidShow, Blog


def add_category(request):
    if request.method=='POST':
        CatForm=CategoryForm(request.POST, request.FILES)
        if CatForm.is_valid():
            CatForm.save()
            return redirect('index')
    else:
        CatForm = CategoryForm()
        return render(request, 'serviceApp/add_Category.html',{'CatForm':CatForm})




def index(request):
    category_list = Category.objects.all()
    slideshow_list=SlidShow.objects.all()
    blog_list=Blog.objects.all()
    len_list=[*range(0, len(slideshow_list), 1)]

    
    
    return render(request, 'serviceApp/MyServices.html',
                  {'category_list':category_list,
                   'first_slid':slideshow_list[0],
                   'slideshow_list':slideshow_list[1:],
                   'len_list':len_list ,
                   'blog_list':blog_list

                   })



def show_category(request, id):
    service_list=Service.objects.all().filter(serv_cat_id=id)
    category_name=Category.objects.all().get(id=id).cat_name
    return render(request, 'serviceApp/list_of_services.html', {'service_list': service_list, 'cat_id': id, 'category_name': category_name})


def add_service(request, id):
    if request.method == 'POST':
        ServForm = ServiceForm(request.POST, request.FILES)
        if ServForm.is_valid():
            ServForm.instance.serv_cat=Category.objects.all().get(id=id)
            ServForm.save()
            return HttpResponseRedirect(reverse('show-category', args=(id,)))
    else:
        ServForm = ServiceForm()
        return render(request, 'serviceApp/Add_Service.html', {'ServForm': ServForm})




def show_service(request,id):
    ser_obj=Category.objects.get(id=id)
    service = Service.objects.filter(serv_cat=ser_obj)
    category_list = Category.objects.all()
    return render(request, 'serviceApp/ServiceView.html', {'ser_obj': ser_obj, 'service': service , 'category_list':category_list})


def view_blog(request,id):
    blog_obj = Blog.objects.get(id=id)
    vid_nam_indx = blog_obj.blog_vid_url.find('be')
    print(vid_nam_indx)
    if vid_nam_indx != -1:
        vid_name = (blog_obj.blog_vid_url[vid_nam_indx + 3:])
    else:
        vid_name = ""
    return render(request, 'serviceApp/blogview.html', {'blog_obj': blog_obj,'vid_name':vid_name})



