
from rest_framework.generics import GenericAPIView
from student.api.v1.serializers import StudentSerializer
from student.models import Student
from rest_framework.response import Response
from rest_framework.views import APIView, Response
from rest_framework.generics import GenericAPIView, get_object_or_404

class StudentAddApi(APIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class StudentUpdateApi(APIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def put(self, request, pk):
        instance = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentDeleteApi(APIView):
    model = Student

    def delete(self, request, pk, format=None):
        student = Student.objects.filter(id=self.kwargs.get('pk'))
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentListApi(APIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)