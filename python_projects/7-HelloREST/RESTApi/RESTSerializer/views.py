from django.http import JsonResponse
from django.shortcuts import render

from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from RESTSerializer.models import Person, Student
from RESTSerializer.serializers import PersonSerializer, StudentSerializer, BookSerializer


class PersonView(View):

    def get(self, request):
        persons = Person.objects.all()
        person_serializer = PersonSerializer(persons, many=True)
        return JsonResponse(person_serializer.data, safe=False)

    def post(self, request):
        p_name = request.POST.get("p_name")
        p_age = request.POST.get("p_age")

        person = Person()
        person.p_name = p_name
        person.p_age = p_age
        person.save()
        person_serializer = PersonSerializer(person)

        return JsonResponse(person_serializer.data)


class StudentView(APIView):

    def post(self, request):
        # s_name = request.POST.get('s_name')
        # s_age = request.POST.get('s_age')
        # student = Student()
        # student.s_name = s_name
        # student.s_age = s_age
        # student.save()
        #
        # student_serializer = StudentSerializer(student)
        # return JsonResponse(student_serializer.data)

        # data = JSONParser().parse(request)
        # return JsonResponse({'msg': 'ok'})

        return Response({'msg': 'ok'}, 201)


@api_view(http_method_names=['GET', 'POST'])
def books(request):
    print(type(request))

    if request.method == 'GET':
        return Response(data={'msg': 'get ok'})
    elif request.method == 'POST':
        print(request.data)
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data)

        return Response(data={'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'msg': '666'})
