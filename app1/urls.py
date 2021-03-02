from django.urls import path
from .views import ContactList, ContactDetailView

urlpatterns= [
    path('', ContactList.as_view(), name= 'contactlist'),
    path('<int:id>', ContactDetailView.as_view(), name= 'contactdetail'),
]