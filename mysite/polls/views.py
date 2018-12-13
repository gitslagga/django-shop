from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, jean. You're at the polls index.")