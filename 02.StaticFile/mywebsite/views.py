from django.shortcuts import render

def index(request):
	context = {
		'tittle'	:'Kelas Terbuka',
		'heading'	:'Selamat datang di',
	}
	return render(request, 'index.html', context)