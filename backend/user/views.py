from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Profile
from .serializers import ProfileSerializer


@api_view(['GET'])
def list_profiles(request):
	if request.user.is_staff:
		profiles = get_list_or_404(Profile)
		serializer = ProfileSerializer(profiles, many=True)
			
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "You are not a staff"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def create_profile(request):
	if request.user.is_staff:
		serializer = ProfileSerializer(data=request.data)
	else:
		return Response({"detail": "You are not a staff"}, status=status.HTTP_403_FORBIDDEN)

	if serializer.is_valid():
		password = serializer.validated_data.pop("password")
		profile = serializer.save()

		profile.set_password(password)
		profile.save()

		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_profile(request, pk):
	if request.user.is_staff:
		profile = get_object_or_404(Profile, id=pk)
	else:
		profile = get_object_or_404(Profile, id=pk, user=request.user)

	serializer = ProfileSerializer(instance=profile, data=request.data)

	if serializer.is_valid():
		password = serializer.validated_data.pop("password")
		serializer.save()

		profile.set_password(password)
		profile.save()

		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail_profile(request, pk):
	if request.user.is_staff:
		profile = get_object_or_404(Profile, id=pk)
	else:
		profile = get_object_or_404(Profile, id=pk, user=request.user)

	serializer = ProfileSerializer(profile)
		
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_profile(request, pk):
	if request.user.is_staff:
		profile = get_object_or_404(Profile, id=pk)
	else:
		profile = get_object_or_404(Profile, id=pk, user=request.user)

	profile.delete()

	return Response({"detail": "Profile has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
