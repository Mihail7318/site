from django.shortcuts import render
from django.http import HttpResponseRedirect

from cust.forms import DocumentForm

from .models import Setting, Standartpages, Faq, Partner, Document


def Upload_file(request):
  if request.method == 'POST':
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/')
  else:
    form =DocumentForm()

  return render(request, 'file_upload.html', {'form': form})



#setting
def Setting(request):
    setting = Setting.objects.all()
    context = {
        'setting': setting,
        'title': 'Главная'
    }
    return render(request, 'base-site/bases.html', context=context )


#head
def head(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    if request.LANGUAGE_CODE == "ru":
        context['title'] = 'head'
    if request.LANGUAGE_CODE == "en":
        context['title'] = 'head'

    return render(request, 'base-site/header/head.html', context=context)


#Document
def document(request):
    document = Document.objects.all()
    context = {
        'document': document,
    }
    if request.LANGUAGE_CODE == "ru":
        context['name'] = 'Документы'
    if request.LANGUAGE_CODE == "en":
        context['name'] = 'Document'
    return render(request, 'cust/document.html', context=context )



#Partner
def partner(request):
    partner = Partner.objects.all()
    context = {
        'partner': partner,
    }
    if request.LANGUAGE_CODE == "ru":
        context['name'] = 'Партнеры'
    if request.LANGUAGE_CODE == "en":
        context['name'] = 'Partner'
    return render(request, 'cust/partner.html', context=context )

#Faq
def faq(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq,
    }
    if request.LANGUAGE_CODE == "ru":
        context['title'] = 'Часто задаваемые вопросы'
    if request.LANGUAGE_CODE == "en":
        context['title'] = 'Frequently Asked Questions'
    return render(request, 'cust/pages/FAQ.html', context=context )



#privacypolicy
def privacypolicy(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    if request.LANGUAGE_CODE == "ru":
        context['title'] = 'Политика  конфиденциальности '
    if request.LANGUAGE_CODE == "en":
        context['title'] = 'Privacy policy'

    return render(request, 'cust/pages/privacypolicy.html', context=context )

#aboutus
def aboutus(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    if request.LANGUAGE_CODE == "ru":
        context['title'] = 'О нас'
    if request.LANGUAGE_CODE == "en":
        context['title'] = 'About'
    return render(request, 'cust/pages/aboutus.html', context=context )

#useragreement
def useragreement(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    if request.LANGUAGE_CODE == "ru":
        context['title'] = 'Пользовательское соглашение'
    if request.LANGUAGE_CODE == "en":
        context['title'] = 'User Agreement'
    return render(request, 'cust/pages/useragreement.html', context=context )

#contact
def contact(request):
    standartpages = Standartpages.objects.get(pk=1)
    context = {
        'standartpages': standartpages,
    }
    if request.LANGUAGE_CODE == "ru":
        context['title'] = 'Контакты'
    if request.LANGUAGE_CODE == "en":
        context['title'] = 'Contact'
    return render(request, 'cust/pages/contact.html', context=context )
