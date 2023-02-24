from django.shortcuts import render
import datetime
# Create your views here.

def filters(request):
    t=datetime.datetime.now()
    d={'data':'THis Is buiLI_in_filTErs','t':t,'c':10}
    return render(request,'filters.html',d)