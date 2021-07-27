from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Fed, Reg

#Fed
def fed(request):
    fed = Fed.objects.all()
    reg = Reg.objects.all()
    context = {
        'feds': fed,
        'reg': reg,
    }
    return render(request, 'konkurs/konkurs.html', context=context )
