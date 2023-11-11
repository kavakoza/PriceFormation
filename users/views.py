from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

# from rest_framework import generics
# from users.models import User
# from users.serializers import UserSerializer
# from rest_framework.permissions import AllowAny
#
#
# class UserCreateAPIView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#
# class UserListAPIView(generics.ListAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#
# class UserRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#
# class UserUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#
# class UserDestroyAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
