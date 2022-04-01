
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student
def mustvowel(value):
    for i in value:
        if(i!='a' or i!='e' or i!='i' or i!='o' or i!='u' or i!='A' or i!='E' or i!='I' or i!='O' or i!='U'):
    # if value[0].lower()!='r':
            raise serializers.ValidationError("Name must contain vowel letter")
        return value

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50,validators=[mustvowel])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)


    def validate_roll(self,value): #field level validation
        if value>=100:
            raise serializers.ValidationError("Roll Must be under 100")
        return value

    def validate(self, data):
        naam=data.get('name')
        rol=data.get('roll')
        ct=data.get('city')
        if naam.lower()=='aakash' and ct.lower()!='pataal':
            raise serializers.ValidationError(" city must be paatal")
        return data

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance