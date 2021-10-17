from django.db import models
import uuid
# Create your models here.
class createbook(models.Model):
    name=models.CharField(max_length=50) 
    img=models.CharField(max_length=200)
    descriptione=models.CharField(max_length=200)
    docfile =models.CharField(max_length=100)


    def __str__(self):
        return self.name
   
class student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
    img=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    


class BookInstance(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
      book = models.ForeignKey('createbook', on_delete=models.SET_NULL, null=True)
      due_back = models.DateField(null=True, blank=True)
    
      STATUS_MAINTENANCE = 'm'
      STATUS_ON_LOAN = 'o'
      STATUS_AVAILABLE = 'a'
      STATUS_RESERVED = 'r'

      LOAN_STATUS = (
    (STATUS_MAINTENANCE, 'Maintenance'),
    (STATUS_ON_LOAN, 'On loan'),
    (STATUS_AVAILABLE, 'Available'),
    (STATUS_RESERVED, 'Reserved'),
    )

      status = models.CharField(
     max_length=1,
     choices=LOAN_STATUS,
     blank=True,
     default='m',
     help_text='Book availability',
  ) 



