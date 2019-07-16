from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from case.models import Case
from case.serializer import CaseSerializer
from account.utils import access_permission
from account.db import get_all_objects
from account.db import get_object

# @access_permission('case_view')

class CaseListView(APIView):
    permission_classes = (IsAuthenticated,)
    model  = Case

    @access_permission('case_view')
    def get(self, request, format=None):
        cases = get_all_objects(self)
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data)


class CaseCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @access_permission('case_create')
    def post(self, request, format=None):
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Case

    @access_permission('case_edit')
    def post(self, request,pk, format=None):
        case = get_object(self,pk)
        serializer = CaseSerializer(case,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseDeleteView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Case

    @access_permission('case_delete')
    def delete(self, request, pk, format=None):
        case = get_object(self,pk)
        case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CaseDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Case

    @access_permission('case_view')
    def get(self, request,pk, format=None):
        case = get_object(self,pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)



