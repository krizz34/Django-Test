from rest_framework import serializers
from medicalStore.models import medic   

class medicSerializer(serializers.ModelSerializer):
    class Meta:
        model = medic
        fields = '__all__'