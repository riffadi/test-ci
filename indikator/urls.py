"""
	Routing URL di aplikasi indikator
"""
from django.urls import path, include
from . import views

app_name = 'indikator'

urlpatterns = [
	path('insikator/', views.indikator, name = 'indikator'),
	path('sasaran/', views.sasaran, name = 'sasaran'),
	path('tujuan/', views.tujuan, name = 'tujuan'),
	path('misi/', views.misi, name = 'misi'),
	path('', views.list, name = 'list'),
]
