from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions, status


class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner= self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


# class ContactAPIView(APIView):
#
#     def get(self,request):
#         phone_object =Contact.objects.all()
#         serializer =ContactSerializer(phone_object,many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ContactSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
