from django.db import models
#from . import virt
from django.contrib.auth.models import AbstractUser


  
class Virtualmachine(models.Model):
    #vmId = models.AutoField
    Name = models.CharField(max_length=50)
    Statut = models.CharField(max_length=50)
    RAM = models.IntegerField()
    Vcpus = models.IntegerField()
    user = models.ForeignKey('Userlist', blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
        

class Userlist(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField(default="")
    vm = models.ManyToManyField(Virtualmachine)
    def __str__(self):
        return self.name
 

class HypervisorDetails(models.Model):

    ip_address = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100,editable=False,null=True)
    uuid = models.CharField(max_length=100,editable=False,null=True)
    memory = models.IntegerField()
    cpucount = models.IntegerField()
    net = models.ForeignKey('NetworkDetails', blank=True, null=True, on_delete=models.CASCADE)
    vm = models.ManyToManyField(Virtualmachine)
    
    def _str_(self):
        return self.ip_address
        

        
class NetworkDetails(models.Model):
    
    ip= models.CharField(max_length=50)
    emplacement = models.CharField(max_length=300)
    netmask = models.CharField(max_length=50)
    vm = models.ManyToManyField(Virtualmachine)
    hyp = models.ForeignKey(HypervisorDetails, blank=True, null=True, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.ip
        
