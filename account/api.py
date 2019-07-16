from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from account.models import User
from account.serializer import UserSerializer
from account.utils import access_permission
from account.db import get_all_objects
from account.db import get_object


class UserListView(APIView):
    permission_classes = (IsAuthenticated,)
    model = User
    
    @access_permission('view_user')
    def get(self, request, format=None):
        users = get_all_objects(self)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

class UserCreateView(APIView):
    permission_classes = (IsAuthenticated,)


    @access_permission('add_user')
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    model = User

    @access_permission('edit_user')
    def post(self, request,pk, format=None):
        user = get_object(self,pk)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    permission_classes = (IsAuthenticated,)
    model =User

    @access_permission('delete_user')
    def delete(self, request, pk, format=None):
        user = get_object(self,pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    model = User

    @access_permission('view_user')
    def get(self, request,pk, format=None):
        user = get_object(self,pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)




    
