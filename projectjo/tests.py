from django.test import TestCase
from django. http import HttpResponse
# Create your tests here.
def Home(request):
    return HttpResponse("HELLO MY PEOPLE")