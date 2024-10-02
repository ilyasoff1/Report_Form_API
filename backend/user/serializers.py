from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ["id", "username", "password", "email", "is_staff", "is_active","is_superuser", "contact", "department"]
