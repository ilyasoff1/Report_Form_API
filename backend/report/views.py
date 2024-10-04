from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Report
from .serializers import ReportSerializer


@api_view(['GET'])
def list_reports(request):
	reports = Report.objects.all()

	if reports and request.user.is_staff:
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "No reports found or you do not have permission"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_report(request):
    serializer = ReportSerializer(data=request.data)
    print(request.user)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_report(request, pk):
	if request.user.is_staff:
		report = Report.objects.get(id=pk)
	else:
		report = Report.objects.get(id=pk, user=request.user)
		
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


# @api_view(['GET'])
# def detail_report(request, pk):
# 	try:
# 		if request.user.is_staff:
# 			report = Report.objects.get(id=pk)
# 		else:
# 			report = Report.objects.get(id=pk, user=request.user)

# 		serializer = ReportSerializer(report)
# 		return Response(serializer.data, status=status.HTTP_200_OK)		
# 	except Report.DoesNotExist:
		
# 	return Response({'detail': 'Report not found or you do not have permission'}, status=status.HTTP_404_NOT_FOUND)
	

@api_view(['GET'])
def user_reports(request):
	reports = Report.objects.filter(user=request.user)

	if reports:
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "No reports found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def admin_reports(request):
	if request.user.is_staff:
		reports = Report.objects.filter(admin=request.user)

	if reports:
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "No reports found"}, status=status.HTTP_404_NOT_FOUND)

	