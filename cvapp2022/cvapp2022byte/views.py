from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.template import loader
from django.urls import reverse
from .forms import PersonForm,DegreeForm
from .models import Person,Degree


def index(request):
	context = {}
	persons = Person.objects.all()
	context['persons'] = persons
	template = 'cvapp2022byte/index.html'
	a = render(request,template,context)
	return a

def person_create(request):
	template = loader.get_template('cvapp2022byte/Person/create.html')
	if request.method == 'POST':		
		form = PersonForm(request.POST, request.FILES)
		file = request.FILES.get('file')
		if form.is_valid():
			form.save()
		else:
			print(form.errors.as_data()) 
		return HttpResponseRedirect(reverse('cvapp_home'))
	else:
		form = PersonForm()
		return HttpResponse(template.render({'form':form},request))

def person_edit(request,pk):
	template = loader.get_template('cvapp2022byte/Person/update.html')
	person = get_object_or_404(Person, pk=pk)
	if request.method == 'POST':		
		form = PersonForm(request.POST,request.FILES,instance=person)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.LastName = request.POST.get('LastName')
			obj.LastName = request.POST.get('FirstName')
			obj.email = request.POST.get('email')
			obj.Mobile = request.POST.get('Mobile')
			degree = get_object_or_404(Degree,pk=request.POST.get('Degree'))
			obj.Degree = degree
			if request.FILES:
				obj.file = request.FILES.get('file')
			obj.save()			
		else:
			print(form.errors.as_data()) 
		return HttpResponseRedirect(reverse('cvapp_home'))
	else:
		form = PersonForm(instance=person)
	return HttpResponse(template.render({'form':form,'person':person},request))

def person_delete(request,pk):
	person = get_object_or_404(Person, pk=pk)
	person.delete()
	return HttpResponseRedirect(reverse('cvapp_home'))
	
def degree_create(request):
	template = loader.get_template('cvapp2022byte/Degree/form.html')
	if request.method == 'POST':
		form = DegreeForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			print(form.errors.as_data()) 
		return HttpResponseRedirect(reverse('cvapp2022byte:degree-list'))
	else:
		form = DegreeForm()
		return HttpResponse(template.render({'form':form},request))

def degree_edit(request,pk):
	template = loader.get_template('cvapp2022byte/Degree/form.html')
	degree = get_object_or_404(Degree, pk=pk)
	if request.method == 'POST':		
		form = DegreeForm(request.POST,instance=degree)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.title = request.POST.get('title')
			obj.save()			
		else:
			print(form.errors.as_data()) 
		return HttpResponseRedirect(reverse('cvapp2022byte:degree-list'))
	else:
		form = DegreeForm(instance=degree)
	return HttpResponse(template.render({'form':form},request))

def degree_delete(request,pk):
	degree = get_object_or_404(Degree, pk=pk)

	try:
		person = Person.objects.get(Degree=degree)		
	except ObjectDoesNotExist:
		degree.delete()
	except MultipleObjectsReturned:
		pass
	
	return HttpResponseRedirect(reverse('cvapp_home'))

def degree_list(request):
	context = {}
	degrees = Degree.objects.all()
	context['degrees'] = degrees
	template = 'cvapp2022byte/Degree/degree_list.html'
	a = render(request,template,context)
	return a

