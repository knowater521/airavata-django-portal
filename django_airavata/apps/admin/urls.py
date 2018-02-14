from django.conf.urls import url

from . import views

app_name = 'admin'
urlpatterns = [
  url(r'^$', views.admin_home, name='admin'),
  url(r'^credential/store$', views.credential_store, name='credential_store'),
  url(r'^compute/resources/', views.compute_resource, name="compute_resource_view"),
]
