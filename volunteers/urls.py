from django.conf.urls import patterns, include, url
import vpms.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import volunteers.views
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'volunteers.views.home', name='home'),
	url(r'^arrived/$', vpms.views.arrived, name="arrived"),
	# url(r'^vpms/', include('vpms.foo.urls')),
	url(r'^enter_name/(?P<project_id>\d+)/$', volunteers.views.enter_name),
	url(r'^joined/(?P<project_id>\d+)/(?P<volunteer_id>\d+)/$', 'volunteers.views.joined'),
	url(r'(?P<volunteer_id>\d+)/$', volunteers.views.info, name='volunteer_info'),
	url(r'^add_project/$', volunteers.views.add_project, name='add_project'),
	url(r'^enter_project/$', volunteers.views.enter_project, name="enter_project"),
#	url(r'^volunteer/', include('volunteers.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
