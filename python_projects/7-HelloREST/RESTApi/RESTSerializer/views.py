from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from RESTSerializer.models import Person
from RESTSerializer.serializers import PersonSerializer


class PersonView(View):
    def get(self, request):
        ...

    def post(self, request):
        p_name = request.POST.get("p_name")
        p_age = request.POST.get("p_age")

        person = Person()
        person.p_name = p_name
        person.p_age = p_age
        person.save()
        person_serializer = PersonSerializer(person)
        print(person_serializer)

        return JsonResponse(person_serializer.data)
