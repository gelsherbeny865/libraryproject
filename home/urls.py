from django.urls import path , include

from home.views import home ,bookdetails,contact,regform,profilestudent,showstudentdetails,signin,search

urlpatterns=[

path('',home,name='home'),
path("book/<int:id>",bookdetails,name='bookdetails'),
path('contact',contact,name='contact'),
path('signup',regform,name="signup"),
path('student/<int:id>',profilestudent ,name="profilestudent"),
path('studentdetails',showstudentdetails,name="studentdetails"),
path('signin',signin ,name="signin"),
path('searchstudent/',search ,name='search')
 

]