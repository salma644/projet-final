from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Virtualmachine,NetworkDetails,HypervisorDetails,Userlist
from django.contrib import messages
import libvirt
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
import sys
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import get_object_or_404
from django.db import models
from django.template.loader import get_template 

def userlist(request):
	user = Userlist.objects.all()
	all_data = Virtualmachine.objects.all()
	context = {
        'all_data': all_data,
        'user': user
        }
	html_template = get_template('index0.html')
	return HttpResponse(html_template.render(context, request))
	#return render(request, 'index0.html',{'user':user})


def base(request):
	return render(request, 'indexacc.html')

def dash(request):
    user_count = Userlist.objects.all().count()
    hyper_count = HypervisorDetails.objects.all().count()
    net_count = NetworkDetails.objects.all().count()
    vm_count = Virtualmachine.objects.all().count()
    
    return render(request,"dash.html",{"user_count":user_count,
    "hyper_count":hyper_count,
    "net_count":net_count,
    "vm_count":vm_count
    })
	

    	
@login_required
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)

			b = Userlist(name=user.username,email=user.email)
			b.save()
			return redirect(userlist)
		
		
		

	context = {'form':form}
	return render(request, 'reg.html', context)

def registerPage(request):
	if request.user.is_authenticated:
		return redirect(index)
		
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = User.objects.create_user(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'],
				email=form.cleaned_data['email']
				)

				b = Userlist(name=user.username,email=user.email)
				b.save()
				return redirect(loginPage)
			
			
			

		context = {'form':form}
		return render(request, 'register.html', context)
		

            

def userdel(request,id):
	user = Userlist.objects.get(id=id)
	b = User.objects.filter(username=user.name)
	b.delete()
	user.delete()
	return redirect(userlist)
	
def userupd(request,id):
	if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']

            if (name=='' or email=='' ):
            	messages.warning(request,"Please fill form Correctly..!")
            else:
            
            	#b = User.objects.filter(username=name)
            	#us = Userlist(name=name, email=email,id=id)
            	#us.save()
            	#b.username=name
            	#b.email=email
            	
            	uss = Userlist(name=name,email=email,id=id)
            	us= User(username=name,email=email)
            	uss.save()

            	#b.username=name
            	#b.email=email
            	#ui.save()
            	#us.save()
            	#user = Userlist.objects.get(id=id)
            	#b = User.objects.get(username=user.name)
            	#u = User(username=name,email=email)
            	#c = Userlist(name=name,email=email)
            	#u.save()
            	#c.save()
            	
            	
            	
            	#user = Userlist.objects.get(id=id)
            	#b = User.objects.get(username=user.name).username
            	#user1 = Userlist(name=name, email=email, id=id)
            	
            	#b = name
            	#c=User(username=b)
            	#c.save()
            	#user1.save()
            	
            	
            	#user1.save()
            	#a1= get_object_or_404(Virtualmachine, id=id)

            	#a2= Userlist()

            	#a2.vm.add(a1)

   
            	
            	
            	
            	messages.success(request,"Data inserted Successfully..!")
            return redirect(userlist)
	
                
            
	
def loginPage(request):
	if request.user.is_authenticated:
		#return render(request,"index.html")
		return redirect(dash)
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				#return render(request,"index.html")
				return redirect(index)
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
  logout(request)
  return redirect(index)
  
def virtual(request):
  all_data = Virtualmachine.objects.all()
  vm = {'all_data':all_data}
  #user = Userlist.objects.all()
  return render(request,"index.html",vm)
  


	
@login_required(login_url='login')
def index(request):
    if request.user.is_superuser:
        all_data = Virtualmachine.objects.all()
        #vm = {'all_data':all_data}
        user = Userlist.objects.all()
        context = {
        'all_data': all_data,
        'user': user
        }
        #html_template = get_template('dash.html')
        #return HttpResponse(html_template.render(context, request))
        return redirect(dash)
       
        #return render(request,"index.html",vm)
    else:
        
        name = request.user.username
        #user = Userlist.objects.filter(name=name)
        user= Userlist.objects.get(name=name)

        user1= user.vm.all()
        #return redirect(userlist)
        return render(request, 'indexvm.html',{'user1':user1})
   
# Insert Data
def insert_data(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Statut = request.POST['Statut']
        RAM = request.POST['RAM']
        Vcpus = request.POST['Vcpus']
        if(Name==''or Statut==''or RAM==''or Vcpus==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            vms = Virtualmachine(Name=Name,Statut=Statut,RAM=RAM,Vcpus=Vcpus)
            vms.save()
            
            xmlconfig = '''
		 <domain type='kvm' id='1'>
		 <name>'''+Name+'''</name>
		 <memory unit='GB'>'''+RAM+'''</memory>
		 <currentMemory unit='GB'>'''+RAM+'''</currentMemory>
		 <vcpu placement='static'>'''+Vcpus+'''</vcpu>
		 <resource>
		   <partition>/machine</partition>
		 </resource>
		 <os>
		   <type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
		   <boot dev='hd'/>
		   </os>
		 <features>
		   <acpi/>
		   <apic/>
		   <pae/>
		 </features>
		 <clock offset='utc'/>
		 <on_poweroff>destroy</on_poweroff>
		 <on_reboot>restart</on_reboot>
		 <on_crash>restart</on_crash>
		 <devices>
		   <emulator>/usr/bin/qemu-system-x86_64</emulator>
		   <disk type='file' device='disk'>
		     <driver name='qemu' type='raw'/>
		     <source file='/home/sy/Downloads/xubuntu-14-14.4.04.1-desktop-i386.iso'/>
		     <backingStore/>
		     <target dev='hda' bus='ide'/>
		     <alias name='ide0-0-0'/>
		     <address type='drive' controller='0' bus='0' target='0' unit='0'/>
		   </disk>
		   <controller type='usb' index='0'>
		     <alias name='usb'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
		     </controller>
		   <controller type='pci' index='0' model='pci-root'>
		     <alias name='pci.0'/>
		   </controller>
		   <controller type='ide' index='0'>
		     <alias name='ide'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
		   </controller>
		   <interface type='network'>
		     <mac address='52:54:00:da:02:01'/>
		     <source network='default' bridge='virbr0'/>
		     <target dev='vnet0'/>
		     <model type='rtl8139'/>
		     <alias name='net0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
		   </interface>
		   <serial type='pty'>
		     <source path='/dev/pts/5'/>
		     <target port='0'/>
		     <alias name='serial0'/>
		   </serial>
		   <console type='pty' tty='/dev/pts/5'>
		     <source path='/dev/pts/5'/>
		     <target type='serial' port='0'/>
		     <alias name='serial0'/>
		   </console>
		   <input type='mouse' bus='ps2'/>
		   <input type='keyboard' bus='ps2'/>
		   <graphics type='vnc' port='5900' autoport='yes' listen='0.0.0.0'>
		     <listen type='address' address='0.0.0.0'/>
		   </graphics>
		   <video>
		     <model type='cirrus' vram='16384' heads='1'/>
		     <alias name='video0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
		   </video>
		   <memballoon model='virtio'>
		     <alias name='balloon0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
		   </memballoon>
		 </devices>
		</domain>
		'''

            conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
            instance = conn.defineXML(xmlconfig)
            messages.success(request,"Data inserted Successfully..!")
	
    #return redirect(index)
    return redirect(virtual)

def insert_data_user(request):
    name = request.user.username
    user= Userlist.objects.get(name=name)
    
    if request.method == "POST":
        Name = request.POST['Name']
        Statut = request.POST['Statut']
        RAM = request.POST['RAM']
        Vcpus = request.POST['Vcpus']
        if(Name==''or Statut==''or RAM==''or Vcpus==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            
            
            xmlconfig = '''
		 <domain type='kvm' id='1'>
		 <name>'''+Name+'''</name>
		 <memory unit='GB'>'''+RAM+'''</memory>
		 <currentMemory unit='GB'>'''+RAM+'''</currentMemory>
		 <vcpu placement='static'>'''+Vcpus+'''</vcpu>
		 <resource>
		   <partition>/machine</partition>
		 </resource>
		 <os>
		   <type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
		   <boot dev='hd'/>
		   </os>
		 <features>
		   <acpi/>
		   <apic/>
		   <pae/>
		 </features>
		 <clock offset='utc'/>
		 <on_poweroff>destroy</on_poweroff>
		 <on_reboot>restart</on_reboot>
		 <on_crash>restart</on_crash>
		 <devices>
		   <emulator>/usr/bin/qemu-system-x86_64</emulator>
		   <disk type='file' device='disk'>
		     <driver name='qemu' type='raw'/>
		     <source file='/home/sy/Downloads/xubuntu-14-14.4.04.1-desktop-i386.iso'/>
		     <backingStore/>
		     <target dev='hda' bus='ide'/>
		     <alias name='ide0-0-0'/>
		     <address type='drive' controller='0' bus='0' target='0' unit='0'/>
		   </disk>
		   <controller type='usb' index='0'>
		     <alias name='usb'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
		     </controller>
		   <controller type='pci' index='0' model='pci-root'>
		     <alias name='pci.0'/>
		   </controller>
		   <controller type='ide' index='0'>
		     <alias name='ide'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
		   </controller>
		   <interface type='network'>
		     <mac address='52:54:00:da:02:01'/>
		     <source network='default' bridge='virbr0'/>
		     <target dev='vnet0'/>
		     <model type='rtl8139'/>
		     <alias name='net0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
		   </interface>
		   <serial type='pty'>
		     <source path='/dev/pts/5'/>
		     <target port='0'/>
		     <alias name='serial0'/>
		   </serial>
		   <console type='pty' tty='/dev/pts/5'>
		     <source path='/dev/pts/5'/>
		     <target type='serial' port='0'/>
		     <alias name='serial0'/>
		   </console>
		   <input type='mouse' bus='ps2'/>
		   <input type='keyboard' bus='ps2'/>
		   <graphics type='vnc' port='5900' autoport='yes' listen='0.0.0.0'>
		     <listen type='address' address='0.0.0.0'/>
		   </graphics>
		   <video>
		     <model type='cirrus' vram='16384' heads='1'/>
		     <alias name='video0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
		   </video>
		   <memballoon model='virtio'>
		     <alias name='balloon0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
		   </memballoon>
		 </devices>
		</domain>
		'''
            vms = Virtualmachine(Name=Name,Statut=Statut,RAM=RAM,Vcpus=Vcpus)
            
            #a1 = get_object_or_404(Userlist,id=request.user.id)
            vms.save()
            user.vm.add(vms)
            conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
            instance = conn.defineXML(xmlconfig)

            
            messages.success(request,"Data inserted Successfully..!")
	
    #return redirect(index)
    return redirect(index)
    

def update_data_user(request,Name,id):
    name = request.user.username
    user= Userlist.objects.get(name=name)
    get_data = Virtualmachine.objects.filter(id=id)
    conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
    domainName = Name
    domain = conn.lookupByName(domainName)
    domain.undefine()
    get_data.delete()
    if request.method == "POST":
        Name = request.POST['Name']
        Statut = request.POST['Statut']
        RAM = request.POST['RAM']
        Vcpus = request.POST['Vcpus']
        if(Name==''or Statut==''or RAM==''or Vcpus==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            xmlconfig = '''
		 <domain type='kvm' id='1'>
		 <name>'''+Name+'''</name>
		 <memory unit='GB'>'''+RAM+'''</memory>
		 <currentMemory unit='GB'>'''+RAM+'''</currentMemory>
		 <vcpu placement='static'>'''+Vcpus+'''</vcpu>
		 <resource>
		   <partition>/machine</partition>
		 </resource>
		 <os>
		   <type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
		   <boot dev='hd'/>
		   </os>
		 <features>
		   <acpi/>
		   <apic/>
		   <pae/>
		 </features>
		 <clock offset='utc'/>
		 <on_poweroff>destroy</on_poweroff>
		 <on_reboot>restart</on_reboot>
		 <on_crash>restart</on_crash>
		 <devices>
		   <emulator>/usr/bin/qemu-system-x86_64</emulator>
		   <disk type='file' device='disk'>
		     <driver name='qemu' type='raw'/>
		     <source file='/home/sy/Downloads/xubuntu-14-14.4.04.1-desktop-i386.iso'/>
		     <backingStore/>
		     <target dev='hda' bus='ide'/>
		     <alias name='ide0-0-0'/>
		     <address type='drive' controller='0' bus='0' target='0' unit='0'/>
		   </disk>
		   <controller type='usb' index='0'>
		     <alias name='usb'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
		     </controller>
		   <controller type='pci' index='0' model='pci-root'>
		     <alias name='pci.0'/>
		   </controller>
		   <controller type='ide' index='0'>
		     <alias name='ide'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
		   </controller>
		   <interface type='network'>
		     <mac address='52:54:00:da:02:01'/>
		     <source network='default' bridge='virbr0'/>
		     <target dev='vnet0'/>
		     <model type='rtl8139'/>
		     <alias name='net0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
		   </interface>
		   <serial type='pty'>
		     <source path='/dev/pts/5'/>
		     <target port='0'/>
		     <alias name='serial0'/>
		   </serial>
		   <console type='pty' tty='/dev/pts/5'>
		     <source path='/dev/pts/5'/>
		     <target type='serial' port='0'/>
		     <alias name='serial0'/>
		   </console>
		   <input type='mouse' bus='ps2'/>
		   <input type='keyboard' bus='ps2'/>
		   <graphics type='vnc' port='5900' autoport='yes' listen='0.0.0.0'>
		     <listen type='address' address='0.0.0.0'/>
		   </graphics>
		   <video>
		     <model type='cirrus' vram='16384' heads='1'/>
		     <alias name='video0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
		   </video>
		   <memballoon model='virtio'>
		     <alias name='balloon0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
		   </memballoon>
		 </devices>
		</domain>
		'''

            vms = Virtualmachine(Name=Name,Statut=Statut,RAM=RAM,Vcpus=Vcpus)
            
            #a1 = get_object_or_404(Userlist,id=request.user.id)
            vms.save()
            user.vm.add(vms)
            conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
            instance = conn.defineXML(xmlconfig)

            
            messages.success(request,"Data inserted Successfully..!")
	
    #return redirect(index)
    return redirect(index)



# Update Data
def update_data(request,Name,id):
    get_data = Virtualmachine.objects.filter(id=id)
    conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
    domainName = Name
    domain = conn.lookupByName(domainName)
    domain.undefine()
    get_data.delete()
    if request.method == "POST":
        Name = request.POST['Name']
        Statut = request.POST['Statut']
        RAM = request.POST['RAM']
        Vcpus = request.POST['Vcpus']
        if(Name==''or Statut==''or RAM==''or Vcpus==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            vms = Virtualmachine(Name=Name,Statut=Statut,RAM=RAM,Vcpus=Vcpus)
            vms.save()
            
            xmlconfig = '''
		 <domain type='kvm' id='1'>
		 <name>'''+Name+'''</name>
		 <memory unit='GB'>'''+RAM+'''</memory>
		 <currentMemory unit='GB'>'''+RAM+'''</currentMemory>
		 <vcpu placement='static'>'''+Vcpus+'''</vcpu>
		 <resource>
		   <partition>/machine</partition>
		 </resource>
		 <os>
		   <type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
		   <boot dev='hd'/>
		   </os>
		 <features>
		   <acpi/>
		   <apic/>
		   <pae/>
		 </features>
		 <clock offset='utc'/>
		 <on_poweroff>destroy</on_poweroff>
		 <on_reboot>restart</on_reboot>
		 <on_crash>restart</on_crash>
		 <devices>
		   <emulator>/usr/bin/qemu-system-x86_64</emulator>
		   <disk type='file' device='disk'>
		     <driver name='qemu' type='raw'/>
		     <source file='/home/sy/Downloads/xubuntu-14-14.4.04.1-desktop-i386.iso'/>
		     <backingStore/>
		     <target dev='hda' bus='ide'/>
		     <alias name='ide0-0-0'/>
		     <address type='drive' controller='0' bus='0' target='0' unit='0'/>
		   </disk>
		   <controller type='usb' index='0'>
		     <alias name='usb'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
		     </controller>
		   <controller type='pci' index='0' model='pci-root'>
		     <alias name='pci.0'/>
		   </controller>
		   <controller type='ide' index='0'>
		     <alias name='ide'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
		   </controller>
		   <interface type='network'>
		     <mac address='52:54:00:da:02:01'/>
		     <source network='default' bridge='virbr0'/>
		     <target dev='vnet0'/>
		     <model type='rtl8139'/>
		     <alias name='net0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
		   </interface>
		   <serial type='pty'>
		     <source path='/dev/pts/5'/>
		     <target port='0'/>
		     <alias name='serial0'/>
		   </serial>
		   <console type='pty' tty='/dev/pts/5'>
		     <source path='/dev/pts/5'/>
		     <target type='serial' port='0'/>
		     <alias name='serial0'/>
		   </console>
		   <input type='mouse' bus='ps2'/>
		   <input type='keyboard' bus='ps2'/>
		   <graphics type='vnc' port='5900' autoport='yes' listen='0.0.0.0'>
		     <listen type='address' address='0.0.0.0'/>
		   </graphics>
		   <video>
		     <model type='cirrus' vram='16384' heads='1'/>
		     <alias name='video0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
		   </video>
		   <memballoon model='virtio'>
		     <alias name='balloon0'/>
		     <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
		   </memballoon>
		 </devices>
		</domain>
		'''

            conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
            instance = conn.defineXML(xmlconfig)
            messages.success(request,"Data updated Successfully..!")
    return redirect(virtual)

def __init__(self, Name):
    self.Name = Name
       
# Delete Data
def delete_data(request,Name,id):
    if request.method == "GET":
        get_data = Virtualmachine.objects.filter(id=id)
        conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
        domainName = Name
        domain = conn.lookupByName(domainName)
        domain.undefine()
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(index)
    
 
       


@login_required(login_url='login')
def index2(request):
    all_data2 = NetworkDetails.objects.all()
    net = {'all_data2':all_data2}
    return render(request,"index2.html",net)
# Insert Data
def insert_datan(request):
    if request.method == "POST":
        ip = request.POST['ip']
        emplacement = request.POST['emplacement']
        netmask = request.POST['netmask']

        if (ip=='' or emplacement=='' or netmask==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            nets = NetworkDetails(ip=ip, emplacement=emplacement, netmask=netmask)
            nets.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(index2)
    # return render(request,"registration/index.html")
# Update Data
def update_datan(request,id):
    if request.method == "POST":
        ip = request.POST['ip']
        emplacement = request.POST['emplacement']
        netmask = request.POST['netmask']

        if (ip=='' or emplacement=='' or netmask==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            nets = NetworkDetails(ip=ip, emplacement=emplacement, netmask=netmask, id=id)
            nets.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(index2)
# Delete Data
def delete_datan(request,id):
    if request.method == "GET":
        get_data = NetworkDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(index2)
    
    
    
@login_required(login_url='login')
def index3(request):
    all_data3 = HypervisorDetails.objects.all()
    hyper = {'all_data3':all_data3}
    return render(request,"index3.html",hyper)
# Insert Data
def insert_datah(request):
    if request.method == "POST":
        ip_address = request.POST['ip_address']
        hostname = request.POST['hostname']
        uuid = request.POST['uuid']
        memory = request.POST['memory']
        cpucount = request.POST['cpucount']
        if (ip_address=='' or hostname=='' or uuid=='' or memory=='' or cpucount==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            hypers = HypervisorDetails(ip_address=ip_address, hostname=hostname, uuid=uuid, memory=memory, cpucount=cpucount)
            hypers.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(index3)
    # return render(request,"registration/index.html")
# Update Data
def update_datah(request,id):
    if request.method == "POST":
        ip_address = request.POST['ip_address']
        hostname = request.POST['hostname']
        uuid = request.POST['uuid']
        memory = request.POST['memory']
        cpucount = request.POST['cpucount']
        if (ip_address=='' or hostname=='' or uuid=='' or memory=='' or cpucount==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            hypers = HypervisorDetails(ip_address=ip_address, hostname=hostname, uuid=uuid, memory=memory, cpucount=cpucount, id=id)
            hypers.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(index3)
# Delete Data
def delete_datah(request,id):
    if request.method == "GET":
        get_data = HypervisorDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(index3)
    
def indexvm(request):
    all_data5 = Virtualmachine.objects.all()
    net = {'all_data5':all_data5}
    conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
    #instance = conn.listDefinedDomains()
    domainName = 'test'
    instance = conn.lookupByName(domainName)
    state, reason = instance.state()
    if state == libvirt.VIR_DOMAIN_RUNNING:
    
        messages.success(request,"is running..!")

    return render(request,"indexvm.html",net)
    
def start(request,Name,id):
    if request.method == "GET":
        get_data = Virtualmachine.objects.filter(id=id)
        conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
        domainName = Name
        domain = conn.lookupByName(domainName)
        domain.create()
        get_data.Statut='running'
        messages.success(request,"vm started Successfully..!")
    return redirect(index)
    
    
def shutdown(request,Name,id):
    if request.method == "GET":
        get_data = Virtualmachine.objects.filter(id=id)
        conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
        domainName = Name
        domain = conn.lookupByName(domainName)
        domain.destroy()
        #b=Virtualmachine(Statut='running')
        messages.success(request, 'vm stoped successfully..!')
    return redirect(index)
