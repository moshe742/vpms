from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib.auth import views as auth_views
import volunteer.views

urlpatterns = [
    # Examples:
    url(r'^$', volunteer.views.home, name='home'),
    url(r'^arrived/$', volunteer.views.arrived, name="arrived"),
    url(r'^accounts/login/$', auth_views.login),
    # url(r'^vpms/', include('vpms.foo.urls')),
    url(r'^add_volunteer/(?P<eknight_id>\d+)/$', volunteer.views.add_volunteer, name='add_volunteer'),
    url(r'^enter_name/(?P<project_id>\d+)/$', volunteer.views.enter_name),
    url(r'^joined/(?P<project_id>\d+)/(?P<volunteer_id>\d+)/$', volunteer.views.joined),
    url(r'welcome/$', volunteer.views.welcome, name='welcome'),
    url(r'volunteer_data/(?P<v_id>\d+)$', volunteer.views.volunteer_data, name='volunteer_data'),
    url(r'date_data/(?P<user_arrived>\d+-\d+-\d+)$', volunteer.views.date_data, name='date_data'),
    url(r'vol_dates/$', volunteer.views.vol_dates, name="vol_dates"),
    url(r'^add_project/$', volunteer.views.add_project, name='add_project'),
    url(r'^enter_project/$', volunteer.views.enter_project, name="enter_project"),
    url(r'^data_insert/$', volunteer.views.data_insert, name='csv2db'),
    url(r'^feedback/$', volunteer.views.feedback, name="feedback"),
]
