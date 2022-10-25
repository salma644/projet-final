from django.contrib import admin

from .models import Virtualmachine,NetworkDetails,HypervisorDetails,Userlist
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm



#admin.site.register(User, UserAdmin)

class VmAdmin(admin.ModelAdmin):
	list_display = ['Name', 'Statut', 'RAM', 'Vcpus']
	


	
class NetworkAdmin(admin.ModelAdmin):
	list_display = ['ip', 'emplacement', 'netmask']
	
class HypervisorAdmin(admin.ModelAdmin):
	list_display = ['ip_address' , 'hostname', 'uuid','memory','cpucount']

class UserlistAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']	
#admin.site.register(Userl)
admin.site.register(Userlist,UserlistAdmin)
admin.site.register(HypervisorDetails,HypervisorAdmin)
admin.site.register(Virtualmachine,VmAdmin)
admin.site.register(NetworkDetails,NetworkAdmin)


