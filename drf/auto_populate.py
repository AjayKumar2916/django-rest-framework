import os

import django
os.environ['DJANGO_SETTINGS_MODULE']='drf.settings'
django.setup()

from contact.models import Contact

contact_data = [
	{'name':'Tom', 'email':'tom@gmail.com', 'phone':'636569858'},
	{'name':'Ben', 'email':'ben@hotmail.com', 'phone':'963656987'},
	{'name':'James', 'email':'james@reddif.com', 'phone':'756585698'},
	{'name':'Peter', 'email':'peter@yahoo.com', 'phone':'7523698758'},
	{'name':'Hunter', 'email':'hunter@ymail.com', 'phone':'9635698785'},
]

for data in contact_data:
	Contact.objects.create(**data)

print "Data populated"