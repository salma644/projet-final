import libvirt

def create():
	try:
		conn = libvirt.open("qemu+ssh://sy@192.168.238.128/system")
		instance = conn.defineXML('templates/vm.xml')
		return instance
	except:
		return None
