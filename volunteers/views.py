# coding: utf8
from django.utils.translation import ugettext as _
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from volunteers.forms import Add_project, Add_volunteer
from volunteers.models import EKnight, Volunteer, Arrival, Expertise, Skill
import json, ast
import datetime, re

def home(request):
	projects = EKnight.objects.all()
	eknights = []
	links = []
	eknights.append({'name': u'הוספת חשמביר', 'level': 'add_eknight'})
	for project in projects:
		volunteers = []
		volunteers.append({'name': u'הוספת מתנדב/ת', 'eknight_id': project.id, 'level': 'add_volunteer'})
		for volunteer in project.volunteers.all():
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
			volunteers.append({'name': v, 'user_id': volunteer.id, 'ekinght_id': project.id, 'color': color, 'arrived': u_arrived, 'signed': u_arrived, 'level': 'volunteer'})
		eknights.append({'name': project.name, 'level': 'project', "children": volunteers})
	eknight = {'name': _('hasadna'), 'level': 'hasadna', 'children': eknights}
	eknight = json.dumps(eknight, ensure_ascii=False)
	return render(request, 'volunteers/home.html', {'eknights': eknight, 'message': 'message', 'links': links})

def arrived(request):
	
	arrive = Arrival.objects.filter(user_arrived=datetime.date.today())
#	volunteers = Volunteer.objects.filter(id=arrive.user_id)
	return render(request, 'volunteers/arrived.html', {'arrived': arrive })

def welcome(request):
	v_id = request.POST['volunteer_id']
	eknight_id = request.POST['eknight']
	coord_message = request.POST['coordinator_message']
	vol_id = Volunteer.objects.get(id=v_id)
	arrived, created = Arrival.objects.get_or_create(user=vol_id, user_arrived=datetime.date.today(), eknight=eknight_id, coordinator_message=coord_message)
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
	form = Add_volunteer(initial={'eknights': eknight_id})
	if request.method == 'POST':
		form = Add_volunteer(request.POST, request.user)
#		form.old_num_of_arrivals=4
#		if request.POST['skill']:
#			skills = re.split('\W+', request.POST['skill'])
#			for sk in skills:
#				enter_skill = Skill(name=sk)
#				enter_skill.full_clean()
#				enter_skill.save()
		if form.is_valid():
			done = form.save()
#			if request.POST['other']:
#				expert = Expertise(name=request.POST['other'])
#				expert.full_clean()
#				expert.save()
#				other_expertise = Expertise.objects.get(name=expert)
#				done.expertise.add(other_expertise.id)
#			user = Volunteer.objects.get(email=done.email)
#			arrival = Arrival(user_id=user)
#			arrival.save()
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

def data_insert(request):
	with open('data', 'rb') as f:
		s = f.read()
		data_dic = ast.literal_eval(s)
		attr_map = {"fname": "first_name", "lname": 'last_name', 'phonenum': 'phone',
					'work_study_place': 'work_study_place', 'emailad': 'email',
					'vol_message': 'volunteer_messages'}
#		assert False, data_dic
		for user_name, user_data in data_dic.iteritems():
			v = Volunteer()
			for key, val in user_data.iteritems():
				if key != 'name' and val:
					if key == 'eknight':
						for date_str, eknight_name in val.iteritems():
							pass
					elif key == 'role':
						expertise = Expertise.objects.filter(name=val)
						val = expertise
					attr = attr_map[key] if key in attr_map else key
					setattr(v, attr, val)
			v.save()
#dic = {}
#    attribute_map = {}
#    for user_name, user_data in dic:
#        v = Volunteer()
#        for key, val in user_data:
#            attr = attribute_map[key] if key in attribute_map else key
#            setattr(v, attr, val)
#        v.save()
#		volunteer = Volunteer(first_name=row[0], last_name=row[1], email=row[3], phone=row[8],
#		home_address=row[9], work_place=row[10], github=row[17], facebook=[18], linkedin=row[19], tweeter=row[20], birth_date=row[21])
#		volunteer.save()
	return HttpResponseRedirect('/')
