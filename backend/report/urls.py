from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.list_reports, name='list-reports'),
	path('myreports/', views.list_my_reports, name='list-my-reports'),
	path('create/', views.create_report, name='create-report'),
	# path('delete/<int:pk>/', views.delete_report, name='delete-report'),
	path('update/<int:pk>/', views.update_report, name='update-report'),
	path('detail/<int:pk>/', views.detail_report, name='detail-report'),
]