from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from serializer.models import User, Position, Departament


class UserSerializer(serializers.ModelSerializer):

    departament = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'position', 'departament')

    def get_departament(self, obj):
        try:
            departament_title = getattr(obj.departament, 'title', None)
        except:
            return 'None'
        return departament_title

    def create(self, validated_data):
        print('password------------')
        validated_data.update({'password': make_password(validated_data.get('password'))})
        return super().create(validated_data)


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class DepartamentSerializer(serializers.ModelSerializer):
    workers = UserSerializer(many=True)

    class Meta:
        model = Departament
        fields = ('title', 'workers')
