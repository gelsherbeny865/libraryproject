from django.shortcuts import render ,get_object_or_404 ,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from home.models import createbook,student,BookInstance
from home.forms import Signup
import datetime
from django.urls import reverse
#from home.forms import Signup
# Create your views here.



def home(request):
    book=createbook.objects.all()
    context={'books':book}
    return render(request,'home/home.html',context)


def bookdetails(request,id):
  books=get_object_or_404(createbook,pk=id)       
  context = {"book":books}
  return render(request, "home/bookdetails.html",context)


    

def contact(request):
  return render(request,'home/contactus.html')

def signup(request):
  print(request)
  print(request.method)
  if request.method == 'GET': 
    return render(request,'home/signup.html')
  elif request.method =='POST':
    student1=student()
    student1.name=request.POST['name']
    student1.email=request.POST['email']
    student1.password=request.POST['password']
    student1.age=request.POST['age']
    student1.address=request.POST['address']
    student1.img=request.POST['img']
    student1.phone=request.POST['phone']
    student1.save()
    return redirect('profilestudent')

#DataFlair #Form #View Functions
def regform(request):
    form1 = Signup()
    if request.method =="GET":
       context={'form1':form1}
       return render(request, 'home/signup.html',context)
    
    elif request.method =='POST':
      student1=student()
      student1.name=request.POST['name']
      student1.email=request.POST['email']
      student1.password=request.POST['password']
      student1.age=request.POST['age']
      student1.address=request.POST['address']
      student1.img=request.POST['img']
      student1.phone=request.POST['phone']
      student1.save()
      return redirect( 'home' )

def showstudentdetails(request):
   std=student.objects.all()
   context={'student':std}
   return render (request,'home/showstudentdetails.html',context)

def profilestudent(request,id):
  students=get_object_or_404(student,pk=id)       
  context = {"student":students}
  return render(request, "home/profilestudent.html",context)

student1=student()
def signin(request):
   if request.method == 'GET': 
     return render(request,'home/signin.html')
   elif request.method =='POST':
    if  (request.POST['email']  and request.POST['password']  ):
      student1.email=request.POST['email']
      student1.password=request.POST['password']
      return redirect('home')
    else:
      return render(request,'home/signin.html')






def search(request):
    status=None   
    if request.GET.get('myform'): # write your form name here 
       
        book_name =  request.GET.get('myform')      
        try:
            status =createbook.objects.filter(bookname__icontains=book_name)
            return render(request,"search.html",{"books":status})
        except:
            return render(request,"search.html",{'books':status})
    else:
       
        return render(request, 'search.html', {'books':status})



