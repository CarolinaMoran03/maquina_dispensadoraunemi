from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
TEMPLATES_DIRS=(
    'os.path.join(BASE_DIR,"templates")'
)
def index(request):
    return render(request, "index.html")

def productos(request):
    return render(request, "productos.html")

def Biribir(request):
    return render(request, "Biribir.html")

def Trululu(request):
    return render(request, "Trululu.html")

def Inake(request):
    return render(request, "Inake.html")