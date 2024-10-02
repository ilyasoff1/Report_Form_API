from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


@api_view(['GET'])
def list_profiles(request):
	profiles = Profile.objects.all()

	if profiles:
		serializer = ProfileSerializer(profiles, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "No profile found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_profile(request):
	serializer = ProfileSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['PUT'])
def update_profile(request, pk):
	profile = Profile.objects.get(id=pk)
	serializer = ProfileSerializer(instance=profile, data=request.data)

	if serializer.is_valid():
		password = serializer.validated_data.pop("password")
		serializer.save()
		profile.set_password(password)
		
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail_profile(request, pk):
	profile = Profile.objects.filter(id=pk).first()

	if profile:
		serializer = ProfileSerializer(profile)
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_profile(request, pk):
	profile = Profile.objects.filter(id=pk).first()

	if profile:
		profile.delete()
		return Response({"detail": "Profile has been deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

	return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)