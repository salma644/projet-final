from django.template.loader import render_to_string

def createVmXML(dictObj):
	return render_to_string('templates/vm.xml',dictObj)
