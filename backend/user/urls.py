from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.list_profiles, name='list-profiles'),
	path('create/', views.create_profile, name='create-profile'),
	path('update/<int:pk>/', views.update_profile, name='update-profile'),
	path('detail/<int:pk>/', views.detail_profile, name='detail-profile'),
	path('delete/<int:pk>/', views.delete_profile, name='delete-profile'),
]