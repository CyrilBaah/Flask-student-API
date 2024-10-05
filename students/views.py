from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.exceptions import NotFound


# class StudentList(GenericAPIView):
#     serializer_class = StudentSerializer

#     def get(self, request):
#         students = Student.objects.all()
#         serializer = self.get_serializer(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentList(APIView):
    """List all students or create a new student"""
    
    serializer_class = StudentSerializer

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    
    serializer_class = StudentSerializer

    def get_object(self, pk):
        """
        Helper method to filter the object with the given pk.
        """
        student = Student.objects.filter(pk=pk).first()  # Get the first match or None
        if student is None:
            raise NotFound(detail="Student not found", code=status.HTTP_404_NOT_FOUND)
        return student

    def get(self, request, pk):
        """
        GET a student by ID.
        """
        student = self.get_object(pk)
        serializer = self.serializer_class(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        PUT (update) a student by ID.
        """
        student = self.get_object(pk)
        serializer = self.serializer_class(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        """
        DELETE a student by ID.
        """
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)