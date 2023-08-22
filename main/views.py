from django.shortcuts import render


def home_page(request):
    return render(request, 'main/home.html')


def contacts_page(request):
    return render(request, 'main/contacts.html')

