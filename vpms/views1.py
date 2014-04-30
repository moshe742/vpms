from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from volunteers.forms import Add_volunteer
from volunteers.models import Volunteer, EKnight
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
		projects = EKnight.objects.filter(name__icontains=name)
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
