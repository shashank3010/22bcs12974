from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re

class StudentAPI(APIView):
    def get(self, request):
        """Returns a predefined operation code"""
        return Response({"operation_code": "ABC123"}, status=status.HTTP_200_OK)

    def post(self, request):
        """Parses the input JSON and processes the required response"""
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            input_string = serializer.validated_data["input_string"]

            # Extract numbers and alphabets
            numbers = [int(char) for char in input_string if char.isdigit()]
            alphabets = [char for char in input_string if char.isalpha()]

            response_data = {
                "status": "Success",
                "user_id": serializer.validated_data["user_id"],
                "college_email": serializer.validated_data["college_email"],
                "college_roll_number": serializer.validated_data["college_roll_number"],
                "numbers_array": numbers,
                "alphabets_array": alphabets,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
