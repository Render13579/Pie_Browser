import urllib2

x = ""

while (x != "exit"):
	y = raw_input("")
	if y != "exit":
		response = urllib2.urlopen("http://" + y)
		page_source = response.read()
		print page_source
	else:
		x = "exit"
