from django.http import HttpResponse
from django.shortcuts import render,redirect

from books.forms import BookForm
from django.template.defaultfilters import title


#
# def home(request):
#     return HttpResponse('home')
# def addbooks(request):
#     return HttpResponse('add books')
# def viewbooks(request):
#     return HttpResponse("View books")

# def home(request):
#     return render(request,'home.html')
from django.views import View
class Home(View):
    def get(self,request):
       return render(request,'home.html')

from books.models import Book
# def addbooks(request):
#     if(request.method=="GET"):
#         form_instance=BookForm()
#         context={'form':form_instance}
#         return render(request,'addbooks.html',context)
#     if(request.method=="POST"):
#         # print(request.POST)
#         # print(request.FILES)
#         form_instance=BookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             # data=form_instance.cleaned_data
#             # b=Book.objects.create(**data)
#             # b.save()
#             form_instance.save()
#             return redirect('books:viewbooks')
class Addbooks(View):
    def get(self,request):
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request,'addbooks.html',context)
    def post(self,request):
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            # data=form_instance.cleaned_data
            # b=Book.objects.create(**data)
            # b.save()
            form_instance.save()
            return redirect('books:viewbooks')
# def viewbooks(request):
#     #processing code to retrieve data
#     b=Book.objects.all()  #returns sequence of db objects/records
#     print(b)
#     context={'books':b}
#     return render(request,"Viewbooks.html",context)
class Viewbooks(View):
    def get(self,request):
        #processing code to retrieve data
        b=Book.objects.all()  #returns sequence of db objects/records
        print(b)
        context={'books':b}
        return render(request,"viewbooks.html",context)
# def detail(request,i):
#     if(request.method=="GET"):
#         b=Book.objects.get(id=i) #returns a single db object/a book record matching with id=i
#         context={'book':b}
#         return render(request,'detail.html',context)
class Detail(View):
    def get(self,request,i):
        b=Book.objects.get(id=i) #returns a single db object/a book record matching with id=i
        context={'book':b}
        return render(request,'detail.html',context)
# def delete(request,i):
#     if (request.method == "GET"):
#         b = Book.objects.get(id=i)
#         b.delete() #deletes the book record
#         return redirect('books:viewbooks')
class Delete(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        b.delete() #deletes the book record
        return redirect('books:viewbooks')
# def edit(request,i):
#     if (request.method == "POST"):
#         b=Book.objects.get(id=i)
#         form_instance=BookForm(request.POST,request.FILES,instance=b)
#
#         if form_instance.is_valid():
#             form_instance.save()
#         return redirect('books:viewbooks')
#
#     if (request.method == "GET"):
#         b = Book.objects.get(id=i)
#         form_instance=BookForm(instance=b)
#         context={'form':form_instance}
#         return render(request, 'edit.html', context)
class Edit(View):
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=BookForm(request.POST,request.FILES,instance=b)

        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:viewbooks')

    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context={'form':form_instance}
        return render(request, 'edit.html', context)

from django.db.models import Q
# def search(request):
#     if(request.method=="GET"):
#         query=request.GET['q']
#         print(query)
#         b=Book.objects.filter(Q(title__icontains=query)|
#                               Q(author__icontains=query)|
#                               Q(price__icontains=query)|
#                               Q(language__icontains=query))
#         context={'books':b}
#         return render(request,"search.html",context)
class Search(View):
    def get(self,request):
        query=request.GET['q']
        print(query)
        b=Book.objects.filter(Q(title__icontains=query)|
                              Q(author__icontains=query)|
                              Q(price__icontains=query)|
                              Q(language__icontains=query))
        context={'books':b}
        return render(request,"search.html",context)













