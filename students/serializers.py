from rest_framework import serializers
from students.models import studen, technologi, project, courses, milestone, info


class studenSerializer(serializers.ModelSerializer):

    class Meta:
        model = studen
        fields = '__all__'

class technologiSerializer(serializers.ModelSerializer):

    class Meta:
        model = technologi
        fields = '__all__'

class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model = project
        fields = '__all__'

class milestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = milestone
        fields = '__all__'

class coursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = courses
        fields = '__all__'


class informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = info
        fields = '__all__'