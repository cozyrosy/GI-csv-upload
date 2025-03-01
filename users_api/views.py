from django.shortcuts import render
import csv
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .models import User
from .serializers import UserSerializer


class UploadCSVView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        
        # Checking if the file is of .csv format.
        if not file.name.endswith('.csv'):
            return Response({"error": "Only CSV files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_file = file.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded_file))
        except Exception:
            return Response({"error": "Invalid CSV file."}, status=status.HTTP_400_BAD_REQUEST)

        valid_records = 0
        invalid_records = 0
        errors = []

        for row in reader:
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                email = row.get('email')
                if not User.objects.filter(email=email).exists():
                    serializer.save()
                    valid_records += 1
                else:
                    errors.append({"email": email, "error": "Duplicate email skipped."})
            else:
                errors.append({"data": row, "errors": serializer.errors})
                invalid_records += 1

        return Response(
            {
                "success": valid_records,
                "failed": invalid_records,
                "errors": errors
            },
            status=status.HTTP_200_OK
        )
