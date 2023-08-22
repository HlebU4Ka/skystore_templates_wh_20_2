from django.urls import path

from main.views import home_page, contacts_page

urlpatterns = [
    path('', home_page),
    path('/', contacts_page)
]