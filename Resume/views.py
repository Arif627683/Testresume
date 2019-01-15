from django.shortcuts import render
from .models import Profail
# Create your views here.
def home(request):
    Pro=Profail.objects.all()
    return render(request,'index.html', {'Pro':Pro})