from django.urls import path , include
from books.views import showallbooks,deletebooks,editbooks,upload_file,borrow_book



urlpatterns=[
    path('add',upload_file,name='addbook'),
    path('showallbooks',showallbooks,name="showallbooks"),
    path('deletebooks/<int:id>',deletebooks , name="deletebooks"),
    path('editbooks/<int:id>',editbooks,name="editbooks"),
    path('',upload_file,name='upload'),
    path('book/<uuid:pk>/borrow/', borrow_book, name='borrow_book'),

]