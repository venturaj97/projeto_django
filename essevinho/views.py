from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. O app EsseVinho está no ar.")