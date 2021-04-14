from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from drfapp.models import DrfModel
# from drfapp.serializer import DrfModelSerializer

from rest_framework import serializers
from drfapp.models import DrfModel


class DrfModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    age = serializers.IntegerField()

    class Meta:
        model = DrfModel
        fields = '__all__'

    def get_fields(self):
        resp = super().get_fields()
        print('get Fields', resp)
        return resp

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        return resp


class RfViewSet(viewsets.ViewSet):

    def dispatch(self, request, *args, **kwargs):
        resp = super().dispatch(request, *args, **kwargs)
        # print('resp: ', type(resp), resp)
        # print(resp.data)
        return resp

    def list(self, request):
        queryset = DrfModel.objects.first()
        serializer = DrfModelSerializer(queryset)
        print('Serializer ----', serializer)
        print(type(serializer))
        return Response(serializer.data)


class MultipleOf:

    def __call__(self, value):
        print('VALUE ', value.get('name'))
        for k, v in value.items():
            print('---->>> ', k, v)


class ModelViewSerializer(serializers.ModelSerializer):
    # validators=[UniqueValidator(queryset=DrfModel.objects.all())]
    name = serializers.CharField(required=True, max_length=123)
    age = serializers.IntegerField(required=True)
    is_gey = serializers.BooleanField(required=True)

    class Meta:
        model = DrfModel
        fields = ('id', 'name', 'age', 'is_gey')
        validators = [MultipleOf()]

    def validate_name(self, value):
        # if value == 'User000':
        #     print('Validate')
        #     raise serializers.ValidationError('Value == User000')

        return value

    # def validate(self, data):
    #     print('Validate 2 fields')
    #     print(self.initial_data)
    #     print(self.instance)
    #     if data['name'] == 'User000' and data['age'] < 20:
    #         raise serializers.ValidationError("if not data['user'] == 'User000' and not data['age'] < 20")
    #     # data['name'] = 'NewUserValid'
    #     # data['age'] = 33
    #     return data



        # validators = [UniqueTogetherValidator(
        #     queryset=DrfModel.objects.all(),
        #     fields=['name', 'age']
        # )]

    # def create(self, validated_data):
    #     resp = super().create(validated_data)
    #     print('create: ', resp)
    #     return resp

    def update(self, instance, validated_data):
        resp = super().update(instance, validated_data)
        print('Instance - ', instance)
        print('Valid_data', validated_data)
        print(resp)
        return resp


class RfModelView(viewsets.ModelViewSet):

    queryset = DrfModel.objects.all()
    serializer_class = ModelViewSerializer

    def create(self, request, *args, **kwargs):
        print('in create')

        serializer = self.get_serializer(data=request.data)
        print(serializer.is_valid())
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        return Response(serializer.data)


    # You can check and what validators is work on Fields
    # print(repr(serializer_class()))

    # if representate fields on Serializer default validators don work

    #  могу явно указать полю например validator=[UniqueValidator]
    # туда выгрузятся все обьекты базы.
    # так понимаю что я могу там явно сделать выборку по каким данным данное поле будет уникальным

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

