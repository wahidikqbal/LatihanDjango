from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'tittle':'About',
		'heading':'Selamat Datang di Halaman',
	
	}
	return render(request,'about/index.html',context)