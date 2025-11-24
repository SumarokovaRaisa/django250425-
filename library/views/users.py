from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from library.models import User
from library.serializers import UserListSerializer, UserCreateSerializer



class UserListCreateGenericView(GenericAPIView):
    queryset = User.objects.all()
    # serializer_class = UserListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer

        return UserCreateSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        users = self.get_queryset()

        if not users:
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = self.get_serializer(users, many=True)  # -> UserListSerializer(...)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )
