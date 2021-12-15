from rest_framework import serializers

from RESTSerializer.models import Person, Student, Book


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    p_name = serializers.CharField(max_length=32)
    p_age = serializers.IntegerField(default=1)
    p_sex = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        instance.p_name = validated_data.get('p_name', instance.p_name)
        instance.p_age = validated_data.get('p_age', instance.p_age)
        instance.p_sex = validated_data.get('p_sex', instance.p_sex)
        instance.save()
        return instance

    def create(self, validated_data):
        Person.objects.create(**validated_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('s_name', 's_age')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('b_name', 'b_price')
