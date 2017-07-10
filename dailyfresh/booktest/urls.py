from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_hies/$', views.register_hies),
    url(r'^login_pwd/$', views.login_pwd),
    url(r'^login_yz/$', views.login_yz),
    url(r'^site/$', views.site),
    url(r'^order/$', views.order),
    url(r'^info/$', views.info),
    url(r'^logout/$', views.logout),



]