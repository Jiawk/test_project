from django.http import HttpResponsr

def index(request):
    return HttpResponse('首页')
