from rest_framework import serializers

from library.models import User



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'role',
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
