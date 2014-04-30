# coding: utf8
from django.utils.translation import ugettext as _
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from volunteers.forms import Add_project, Add_volunteer
from volunteers.models import EKnight, Volunteer, Arrival, Expertise, Skill
import json
import csv
import datetime, re

def home(request):
	projects = EKnight.objects.all()
	eknights = []
	links = []
	eknights.append({'name': u'הוספת חשמביר', 'level': 'add_eknight'})
	for project in projects:
		volunteers = []
		volunteers.append({'name': u'הוספת מתנדב/ת', 'eknight_id': project.id, 'level': 'add_volunteer'})
		for volunteer in project.volunteer.all():
			arrival = Arrival.objects.filter(user_id=volunteer.id, user_arrived=datetime.date.today())
			v = volunteer.first_name + " " + volunteer.last_name
			u_arrived = str()
			color = str()
			if arrival:
				u_arrived = True
				color = '#08ff00'
			else:
				u_arrived = False
				color = '#ff4646'
			volunteers.append({'name': v, 'user_id': volunteer.id, 'color': color, 'arrived': u_arrived, 'signed': u_arrived, 'level': 'volunteer'})
		eknights.append({'name': project.name, 'level': 'project', "children": volunteers})
	eknight = {'name': _('hasadna'), 'level': 'hasadna', 'children': eknights}
	eknight = json.dumps(eknight, ensure_ascii=False)
	return render(request, 'volunteers/home.html', {'eknights': eknight, 'message': 'message', 'links': links})

def arrived(request):
	
	arrive = Arrival.objects.filter(user_arrived=datetime.date.today())
#	volunteers = Volunteer.objects.filter(id=arrive.user_id)
	return render(request, 'volunteers/arrived.html', {'arrived': arrive })

def welcome(request):
	v_id = request.GET['volunteer_id']
	vol_id = Volunteer.objects.get(id=v_id)
	arrived, created = Arrival.objects.get_or_create(user_id=vol_id, user_arrived=datetime.date.today())
	if not created:
		arrived.delete()
	return HttpResponse('success')

def add_project(request):
	project_list = EKnight.objects.all().order_by('name')
	form = Add_project()
	if request.method == 'POST':
		form_filled = Add_project(request.POST, request.user)
		if form_filled.is_valid():
			clean_form = form_filled.cleaned_data
			added = EKnight(name=clean_form['name'])
			added.save()
			return HttpResponseRedirect('/')
	return render(request, 'volunteers/add_project.html', {'form': form, 'project_list': project_list})


def add_volunteer(request, eknight_id):
	form = Add_volunteer(initial={'eknight_vol': eknight_id})
	if request.method == 'POST':
		form = Add_volunteer(request.POST, request.user)
#		if request.POST['skill']:
#			skills = re.split('\W+', request.POST['skill'])
#			for sk in skills:
#				enter_skill = Skill(name=sk)
#				enter_skill.full_clean()
#				enter_skill.save()
		if form.is_valid():
			done = form.save()
			if request.POST['other']:
				expert = Expertise(name=request.POST['other'])
				expert.full_clean()
				expert.save()
				other_expertise = Expertise.objects.get(name=expert)
				done.expertise.add(other_expertise.id)
			user = Volunteer.objects.get(email=done.email)
			arrival = Arrival(user_id=user)
			arrival.save()
			return HttpResponseRedirect('/')
	return render(request, 'volunteers/add_volunteer.html', {'form': form})


def enter_project(request):
	project_list = EKnight.objects.all().order_by('name')
	return render(request, 'volunteers/enter_project.html', {'project_list': project_list})

def enter_name(request, project_id):
	name = Volunteer.objects.all().order_by('name')
	project = get_object_or_404(EKnight, pk=project_id)
	return render(request, 'volunteers/enter_name.html', {'name_list': name, 'project': project})

def joined(request, project_id, volunteer_id):
	html = "you %s vol entered project %s" % (volunteer_id, project_id)
	return HttpResponse(html)
	return render(request, "you %s vol entered project" % project_id)

def csv2db(request):
	csv_file = open('VOL12.csv', 'rb')
	csv_data = csv.reader(csv_file)
	for row in csv_data:
		volunteer = Volunteer(first_name=row[0], last_name=row[1], email=row[3], phone=row[8],
		home_address=row[9], work_place=row[10], github=row[17], facebook=[18], linkedin=row[19], tweeter=row[20], birth_date=row[21])
		volunteer.save()
	return HttpResponseRedirect('/')
