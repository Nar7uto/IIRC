from django.shortcuts import render
from .form import SignUpForm
from .form import ContactForm

def home(request):
	return render(request, 'home.html', {})

def index(request):
	
	title = "Welcome guest"
	form = SignUpForm(request.POST or None)
	if request.user.is_authenticated:
		title = "Welcome %s" %(request.user)
	context = { 
		'title':title,
		'myName': 'Hasan',
		'form':form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.fullname:
			email_base, provider = instance.email.split('@')
			instance.fullname = email_base
			instance.save()
		context = { 
			'title': 'Thank for Registeration',
		}
	return render(request, 'index.html', context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		fullname = form.cleaned_data.get('fullname')

	context = {
		'form': form,
	}
	return render(request, 'forms.html', context)
