
from django.shortcuts import render,redirect,HttpResponse
from onlinebus.models import bus,consumer
from onlinebus.forms import busform,consumerform,contactform
from django.contrib import admin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import contactform



def add_post(request):
    try:
        entry_title = request.POST["title"]
    except KeyError:
        entry_title = "Guest"
    return HttpResponse('Hello %s' % entry_title)


def display_view(request):
    ticket1=bus.objects.all()
    return render(request,"onlinebus/display.html",{"ticket1":ticket1})

def add_view(request):
    form=busform()
    if request.method =='POST':
        form=busform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display')

    return render(request,'onlinebus/create.html',{'form':form})

def update_view(request,id):

    bus_data = bus.objects.get(id=id)
    if request.method =='POST':

        bus_name=request.POST["bus_name"]
        bus_num=request.POST["bus_num"]
        start=request.POST["start"]
        end=request.POST["end"]
        seats=request.POST["seats"]
        balanseat=request.POST["balanseat"]
        amount=request.POST["amount"]
        date=request.POST["date"]
        time=request.POST["time"]
        bus_data.bus_name = bus_name
        bus_data.bus_num = bus_num
        bus_data.start = start
        bus_data.end = end
        bus_data.seats = seats
        bus_data.balanseat = balanseat
        bus_data.amount=amount
        bus_data.date = date
        bus_data.time = time
        bus_data.save()

        return redirect('/display')
    return render(request,'templates/onlinebus/update.html',{"bus_data":bus_data})

def delete_view(request ,id):
    bus_data = bus.objects.get(id=id)
    bus_data.delete()
    return redirect('/display')

def consumerdisplay_view(request):
    info=consumer.objects.all()
    return render(request,"onlinebus/consumer_display.html",{"info":info})


def consumer_view(request):
    form=consumerform()
    if request.method =='POST':
        form=consumerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/consumerdisplay')

    return render(request,'onlinebus/consumer.html',{'form':form})

def deleteconsumer_view(request ,id):
    info =consumer.objects.get(id=id)
    info.delete()
    return redirect('/consumerdisplay')

def updateconsumer_view(request, id):
        consumer_data = consumer.objects.get(id=id)
        if request.method == ('POST'):
            name = request.POST["name"]
            age= request.POST["age"]
            address=request.POST['address']
            phone=request.POST['phone']
            start = request.POST["start"]
            end = request.POST["end"]
            date = request.POST["date"]
            time = request.POST["time"]
            consumer_data.name = name
            consumer_data.age = age
            consumer_data.address = address
            consumer_data.phone = phone
            consumer_data.start= start
            consumer_data.end = end
            consumer_data.date = date
            consumer_data.time = time
            consumer_data.save()
            return redirect('/consumerdisplay')
        return render(request, 'onlinebus/updateconsumer.html', {"consumer_data": consumer_data})



def index_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('onlinebus/index.html', {
                'name': name,
                'email': email,
                'content': content,
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['udayajone@gmail.com'], fail_silently=False,)

            return redirect('/index')
    else:
        form = contactform()

    return render(request, 'onlinebus/index.html', {'form': form })