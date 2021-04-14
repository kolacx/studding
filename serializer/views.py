from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from serializer.models import User, Position, Departament
from serializer.serializer import UserSerializer, PositionSerializer, DepartamentSerializer


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False, url_path='user/(?P<id>[^/.]+)')
    def get_user(self, request, *args, **kwargs):
        context = self.get_queryset().filter(id=kwargs.get('id'))
        serializer = self.serializer_class(context, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, url_path='user')
    def post_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        # self.perform_create(serializer)
        serializer.save()
        return Response(serializer.data)
        # return super().create(request, *args, **kwargs)

    @action(methods=['post'], detail=False, url_path='user/change_password')
    def change_password(self, request, *args, **kwargs):
        


        return Response('res')


class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class DepartamentView(viewsets.ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
