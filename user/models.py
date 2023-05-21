from email.headerregistry import Address
from django.db import models


# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=200)
    fName = models.CharField(max_length=200)
    lName = models.CharField(max_length=200)
    role = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.userName

class Host(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #profile
    profile=models.ImageField(upload_to='images/hosts')
    

    def __str__(self):
         return self.user.userName

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=200)
    about = models.TextField(null=True)
    #profile
    profile=models.ImageField(upload_to='images/clients',null=True)
    

    def __str__(self):
         return self.user.userName


class Erreur(models.Model):
    url = models.CharField(max_length=200)
    erreur_date=models.DateTimeField(auto_now_add=True, blank=True)
    erreur = models.TextField()

    def __str__(self):
        return self.url+" | date : "+str(self.erreur_date.year)+"-"+str(self.erreur_date.month)+"-"+str(self.erreur_date.day)