from django import forms


class Signup(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    img=forms.CharField(max_length=200)
    password=forms.CharField(max_length=50)
    phone=forms.CharField(max_length=20)
    address=forms.CharField(max_length=30)

 
class books(forms.Form):
    name=forms.CharField(max_length=50) 
    img=forms.CharField(max_length=200)
    descriptione=forms.CharField(max_length=200)
    docfile = forms.CharField(max_length=100)

