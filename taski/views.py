from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import *
from .forms import *


# получение данных из бд
def index(request):
    zadacha = Zadacha.objects.all()
    return render(request, "taski/listtaski.html", {"zadacha": zadacha})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        zadacha = Zadacha()
        zadacha.title = request.POST.get("title")
        zadacha.age = request.POST.get("age")
        zadacha.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):

    try:
        zadacha = Zadacha.objects.get(id=id)

        if request.method == "POST":
            zadacha.title = request.POST.get("title")
            zadacha.age = request.POST.get("age")
            zadacha.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "taski/redtaski.html", {"zadacha": zadacha})
    except Zadacha.DoesNotExist:
        return HttpResponseNotFound("<h2>Zadacha not found</h2>")



# удаление данных из бд
def delete(request, id):
    try:
        zadacha = Zadacha.objects.get(id=id)
        zadacha.delete()
        return HttpResponseRedirect("/")
    except Zadacha.DoesNotExist:
        return HttpResponseNotFound("<h2>Zadacha not found</h2>")


def addtaski(request):
    error = ''
    if request.method == 'POST':
        addtaski = TaskiForm(request.POST)
        if addtaski.is_valid():
            addtaski.save()
            slug = request.POST.get("slug")
            post = Post.objects.get(slug=slug)
            print(post)
            if post is None:
                print("none")
                return HttpResponseRedirect(request.path_info)
            else:
                error = 'Занято'
        else:
            error = 'Форма была не верна заполнена'

    addtaski = TaskiForm()

    data = {
        'addtaski': addtaski,
        'error' : error
    }

    return render(request, 'taski/addtaski.html', data)