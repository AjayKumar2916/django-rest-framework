from django.conf.urls import url

from contact.views import *

urlpatterns = [
    # Contact List
    url(r'api/contact/list/$', ContacttList.as_view()),

    # Add Contact
    url(r'api/contact/add/$', AddContact.as_view()),

    # Retrieve Contact
    url(r'api/contact/(?P<pk>[0-9]+)/$', RetrieveContact.as_view()),

    # Edit Contact
    url(r'api/contact/(?P<pk>[0-9]+)/edit/$', EditContact.as_view()),

    # Delete Contact
    url(r'api/contact/(?P<pk>[0-9]+)/delete/$', DeleteContact.as_view()),
]