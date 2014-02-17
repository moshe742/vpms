from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from volunteers.forms import Add_project, Add_volunteer
from volunteers.models import Project, Volunteer
import datetime

def home(request):
	form = Add_volunteer()
	if 'volunteer' in request.GET and request.GET['volunteer']:
		name = request.GET['volunteer']
		users = Volunteer.objects.filter(name__icontains=name, arrived__lt=datetime.datetime.now())
		return render(request, 'home.html', {'searched': name, 'users': users, 'form': form})
	elif 'user_name' in request.GET and request.GET['user_name']:
		volunteer_id = Volunteer.objects.get(id=request.GET['user_name']).save()
	elif 'project' in request.GET and request.GET['project']:
		name = request.GET['project']
		projects = Project.objects.filter(name__icontains=name)
		return render(request, 'home.html', {'form': form, 'search_project': name, 'projects': projects})
	elif request.method == 'POST':
		form = Add_volunteer(request.POST, request.user)
		if form.is_valid():
			clean_form = form.cleaned_data
			added = Volunteer(name=clean_form['name'], email=clean_form['email'], phone=clean_form['phone'])
			added.save()
	return render(request, 'home.html', {'form': form})

def arrived(request):
	
	arrived = Volunteer.objects.filter(arrived=datetime.date.today())
	return render(request, 'arrived.html', {'arrived': arrived })

def info(request, volunteer_id):
	volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
	return render(request, 'volunteers/volunteer_details.html', {'volunteer': volunteer})

def add_project(request):
	project_list = Project.objects.all().order_by('name')
	form = Add_project()
	if request.method == 'POST':
		form_filled = Add_project(request.POST, request.user)
		if form_filled.is_valid():
			clean_form = form_filled.cleaned_data
			added = Project(name=clean_form['name'])
			added.save()
			return HttpResponseRedirect('/')
	return render(request, 'volunteers/add_project.html', {'form': form, 'project_list': project_list})

def enter_project(request):
	project_list = Project.objects.all().order_by('name')
	return render(request, 'volunteers/enter_project.html', {'project_list': project_list})

def enter_name(request, project_id):
	name = Volunteer.objects.all().order_by('name')
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'volunteers/enter_name.html', {'name_list': name, 'project': project})

def joined(request, project_id, volunteer_id):
	html = "you %s vol entered project %s" % (volunteer_id, project_id)
	return HttpResponse(html)
	return render(request, "you %s vol entered project" % project_id)
