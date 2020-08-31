from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url('save_pd', views.save_pd, name='save_pd'),
    url('save_pp', views.save_pp, name= 'save_pp'),
    url('save_e', views.save_e, name= 'save_e'),
    url('edit_e', views.edit_e, name='edit_e'),
    url('save_i', views.save_i, name='save_i'),
    url('edit_i', views.edit_i, name='edit_i'),
    url('save_r', views.save_r, name='save_r'),
    url('edit_r', views.edit_r, name='edit_r'),
    url('save_we', views.save_we, name='save_we'),
    url('edit_we', views.edit_we, name='edit_we')
]
