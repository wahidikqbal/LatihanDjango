from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
	'tittle'	:'Blog',
	'heading'	:'Ini adalah Halaman',
	}
	return render(request,'blog/index.html',context)