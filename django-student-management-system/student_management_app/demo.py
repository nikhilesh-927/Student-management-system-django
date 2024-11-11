from django.http import HttpResponse 

def my_view(request):
    if request.method == 'GET':
        return HttpResponse("How is it going world!")