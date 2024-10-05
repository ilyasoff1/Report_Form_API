from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Report
from .serializers import ReportSerializer


@api_view(['GET'])
def list_reports(request):
	if request.user.is_staff:
		reports = get_list_or_404(Report)

		serializer = ReportSerializer(reports, many=True)
		
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "You are not a staff"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def create_report(request):
    serializer = ReportSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_report(request, pk):
	if request.user.is_staff:
		report = get_object_or_404(Report, id=pk)
	else:
		report = get_object_or_404(Report, id=pk, user=request.user)
		
	serializer = ReportSerializer(instance=report, data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail_report(request, pk):
	if request.user.is_staff:
		report = get_object_or_404(Report, id=pk)
	else:
		report = get_object_or_404(Report, id=pk, user=request.user)

	serializer = ReportSerializer(report)

	return Response(serializer.date, status=status.HTTP_200_OK)
	

@api_view(['GET'])
def user_reports(request):
	reports = get_list_or_404(Report, user=request.user)
	serializer = ReportSerializer(reports, many=True)

	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def admin_reports(request):
	if request.user.is_staff:
		reports = get_list_or_404(Report, admin=request.user)
		serializer = ReportSerializer(reports, many=True)
		
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "You are not a staff"}, status=status.HTTP_403_FORBIDDEN)
