from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from home.models import createbook ,BookInstance
from home.forms import books
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def addbook(request):
  print(request)
  print(request.method)
  if request.method == 'GET': 
    return render(request,'books/addbook.html')
  elif request.method =='POST':
    print(request.POST['name'])
    book=createbook()
    book.name=request.POST['name']
    book.img=request.File['img']
    book.descriptione=request.POST['desc']
    book.docfile=request.POST['file']
    book.save()
    return redirect('home')
   
    


def showallbooks(request):
  books=createbook.objects.all()    
  context = {"book":books}
  return render(request,'books/showbooks.html' ,context)


def deletebooks(request,id):
  book=get_object_or_404(createbook,pk=id)
  book.delete()
  return redirect('showallbooks')

def editbooks(request,id):
  book=get_object_or_404(createbook,pk=id)
  if request.method =="GET":
     context={'books':book}
     return render(request,'books/editbook.html',context)
  elif request.method =="POST":
    book.name=request.POST['name']
    book.img=request.POST['img']
    book.descriptione=request.POST['desc']
    book.save()
    return redirect('showallbooks')



def upload_file(request):
    if request.method == 'POST':
        form = books(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return books('/success/url/')
    else:
        form = books()
    return render(request, 'books/addbook.html', {'form': form})



def borrow_book(request, pk):
   book_instance = get_object_or_404(BookInstance, pk=pk)
   if request.method == 'POST':
        if request.user.is_authenticated:
            book_instance.borrower = request.user
            book_instance.due_back = datetime.date.today() + datetime.timedelta(weeks=3)
            book_instance.status = 'STATUS_ON_LOAN'
            book_instance.save()
            return HttpResponseRedirect(reverse('dashboard_customer'))

   context = {
       'book_instance': book_instance,
    }

   return render(request, 'home/book_detail.html', context)