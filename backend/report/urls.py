from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.list_reports, name='list-reports'),
	path('create/', views.create_report, name='create-report'),
	path('user-reports/', views.user_reports, name='user-reports'),
	path('admin-reports/', views.admin_reports, name='admin-reports'),
	path('update/<int:pk>/', views.update_report, name='update-report'),
	path('detail/<int:pk>/', views.detail_report, name='detail-report'),

]