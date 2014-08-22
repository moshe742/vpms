from django.conf.urls import patterns, include, url
import volunteers.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import volunteers.views
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'volunteers.views.home', name='home'),
	url(r'^arrived/$', volunteers.views.arrived, name="arrived"),
	# url(r'^vpms/', include('vpms.foo.urls')),
	url(r'^add_volunteer/(?P<eknight_id>\d+)/$', volunteers.views.add_volunteer, name='add_volunteer'),
	url(r'^enter_name/(?P<project_id>\d+)/$', volunteers.views.enter_name),
	url(r'^joined/(?P<project_id>\d+)/(?P<volunteer_id>\d+)/$', 'volunteers.views.joined'),
	url(r'welcome/$', volunteers.views.welcome, name='welcome'),
	url(r'volunteer_data/(?P<v_id>\d+)$', volunteers.views.volunteer_data, name='volunteer_data'),
	url(r'date_data/(?P<user_arrived>\d+-\d+-\d+)$', volunteers.views.date_data, name='date_data'),
	url(r'vol_dates/$', volunteers.views.vol_dates, name="vol_dates"),
	url(r'^add_project/$', volunteers.views.add_project, name='add_project'),
	url(r'^enter_project/$', volunteers.views.enter_project, name="enter_project"),
	url(r'^data_insert/$', volunteers.views.data_insert, name='csv2db'),
	url(r'^feedback/$', volunteers.views.feedback, name="feedback"),
#	url(r'^volunteer/', include('volunteers.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
