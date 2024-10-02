from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer


@api_view(['GET'])
def list_reports(request):
	reports = Report.objects.filter(user=request.user)

	if reports.exists():
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response({"detail": "No reports found"}, status=HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_report(request):
    serializer = ReportSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_report(request, pk):
	report = Report.objects.get(id=pk, user=request.user)
	serializer = ReportSerializer(instance=report, data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail_report(request, pk):
	report = Report.objects.filter(id=pk, user=request.user).first()

	if report:
		serializer = ReportSerializer(report)
		return Response(serializer.data, status=status.HTTP_200_OK)
		
	return Response({'detail': 'Report not found'}, status=status.HTTP_404_NOT_FOUND)
	

# @api_view(['DELETE'])
# def delete_report(request, pk):
# 	report = Report.objects.filter(id=pk, user=request.user).first()

# 	if report:  
# 		report.delete()
# 		return Response({'detail': 'Report has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# 	return Response({'detail': 'Report not found'}, status=status.HTTP_404_NOT_FOUND)

	