from django.db import models

# Create your models here.

class UserSignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class NotesData(models.Model):
    tech=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    notesfile=models.FileField(upload_to='Notes')
    
    
    