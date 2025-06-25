from django.shortcuts import render

# Create your views here.
def contacts_home(request):

    return render(request, "contacts/contacts.html")