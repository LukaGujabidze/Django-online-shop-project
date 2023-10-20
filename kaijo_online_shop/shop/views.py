from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def shop(request):
    template = loader.get_template('shop.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def cloth(request):
    template = loader.get_template('cloth.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def toys(request):
    template = loader.get_template('toys.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def perfume(request):
    template = loader.get_template('perfume.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def electrics(request):
    template = loader.get_template('electrics.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def deals(request):
    template = loader.get_template('deals.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def account(request):
    template = loader.get_template('account.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def contact(request):
    template = loader.get_template('contact.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def about(request):
    template = loader.get_template('about.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def privacy(request):
    template = loader.get_template('privacy.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def register(request):
    template = loader.get_template('register.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def sign_in(request):
    template = loader.get_template('sign_in.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)

def cart(request):
    template = loader.get_template('cart.html')
    rendered_template = template.render()
    return HttpResponse(rendered_template)


