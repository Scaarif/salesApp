from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context=context)

def login_view(request):
    context = {}
    return render(request, "login.html", context=context)