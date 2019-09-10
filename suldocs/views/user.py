from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from suldocs.models.user import (
    User as UserModel,
    UsersSerializer
)


class User(APIView):
    def get(self, request):
        users = self.get_users_from_db(request)

        return Response(users.data)

    def post(self, request):
        user_data = request.data
        email = user_data.get("email")
        if self.__exists_email(email):
            return Response(status=HTTPStatus.BAD_REQUEST)

        password = user_data.get("password")
        UserModel.objects.create_user(email=email, password=password)

        return Response({"email": email})

    @staticmethod
    def get_users_from_db(request):
        users = UserModel.objects.all()
        print(users)
        return UsersSerializer(users, many=True)

    @staticmethod
    def __exists_email(email):
        return UserModel.objects.filter(email=email).exists()
