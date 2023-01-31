
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):

    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-created']


    def __str__(self):
        return self.body[0:50]


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=15)
    

    
    def __str__(self):
        return self.user.username



class Contact(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id