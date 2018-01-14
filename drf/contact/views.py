# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework.generics import (
										ListAPIView,
										CreateAPIView,
										RetrieveAPIView,
										UpdateAPIView,
										DestroyAPIView
									)

from contact.models import Contact
from contact.serializers import ContactSerializer

# Contact List
class ContacttList(ListAPIView):
	queryset = Contact.objects.all().order_by('-id')
	serializer_class = ContactSerializer

# Add Contact
class AddContact(CreateAPIView):
	queryset = Contact.objects.all().order_by('-id')
	serializer_class = ContactSerializer

# Retrieve Contact
class RetrieveContact(RetrieveAPIView):
	queryset = Contact.objects.all().order_by('-id')
	serializer_class = ContactSerializer

# Edit Contact
class EditContact(UpdateAPIView):
	queryset = Contact.objects.all().order_by('-id')
	serializer_class = ContactSerializer

# Delete Contact
class DeleteContact(DestroyAPIView):
	queryset = Contact.objects.all().order_by('-id')
	serializer_class = ContactSerializer

