from email.message import EmailMessage
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from onlinebus.forms import busform, consumerform
from onlinebus.models import bus, consumer
from .forms import contactform
from django.core.mail import EmailMessage

"""def add_post(request):
    try:
        entry_title = request.POST["title"]
    except KeyError:
        entry_title = "Guest"
    return HttpResponse('Hello %s' % entry_title)"""


def display_view(request):
    ticket1 = bus.objects.all()
    return render(request, "onlinebus/display.html", {"ticket1": ticket1})


def add_view(request):
    form = busform()
    if request.method == 'POST':
        form = busform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display')

    return render(request, 'onlinebus/create.html', {'form': form})


def update_view(request, id):
    bus_data = bus.objects.get(id=id)
    if request.method == 'POST':
        bus_name = request.POST.get["bus_name"]
        bus_no = request.POST.get["bus_no"]
        start = request.POST.get["start"]
        end = request.POST.get["end"]
        seats = request.POST.get["seats"]
        balanseat = request.POST.get["balanseat"]
        amount = request.POST.get["amount"]
        date = request.POST.get["date"]
        time = request.POST.get["time"]
        bus_data.bus_name = bus_name
        bus_data.bus_no = bus_no
        bus_data.start = start
        bus_data.end = end
        bus_data.seats = seats
        bus_data.balanseat = balanseat
        bus_data.amount = amount
        bus_data.date = date
        bus_data.time = time
        bus_data.save()

        return redirect('/display')
    return render(request, 'onlinebus/update.html', {"bus_data": bus_data})


def delete_view(request, id):
    bus_data = bus.objects.get(id=id)
    bus_data.delete()
    return redirect('/display')


def consumerdisplay_view(request):
    info = consumer.objects.all()
    return render(request, "onlinebus/consumer_display.html", {"info": info})


def consumer_view(request):
    form = consumerform()
    if request.method == 'POST':
        form = consumerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/consumerdisplay')

    return render(request, 'onlinebus/consumer.html', {'form': form})


def deleteconsumer_view(request, id):
    info = consumer.objects.get(id=id)
    info.delete()
    return redirect('/consumerdisplay')


def updateconsumer_view(request, id):
    consumer_data = consumer.objects.get(id=id)
    if request.method == ('POST'):
        name = request.POST["name"]
        age = request.POST["age"]
        address = request.POST['address']
        phone = request.POST['phone']
        start = request.POST["start"]
        end = request.POST["end"]
        date = request.POST["date"]
        time = request.POST["time"]
        consumer_data.name = name
        consumer_data.age = age
        consumer_data.address = address
        consumer_data.phone = phone
        consumer_data.start = start
        consumer_data.end = end
        consumer_data.date = date
        consumer_data.time = time
        consumer_data.save()
        return redirect('/thank')
    return render(request, 'onlinebus/updateconsumer.html', {"consumer_data": consumer_data})

def thank(request):
    return render(request,"onlinebus/thank.html")


def index_view(request):
        if request.method == 'POST':
            form = contactform(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                email = form.cleaned_data['email']
                address = form.cleaned_data['address']
                contact_no = form.cleaned_data['contact_no']
                start = form.cleaned_data['start']
                end = form.cleaned_data['end']
                date = form.cleaned_data['date']
                time = form.cleaned_data['time']
                content = form.cleaned_data['content']

                html = render_to_string('onlinebus/index.html', {
                    'name': name,
                     'age': age,
                    'email': email,
                    'address': address,
                    'contact_no': contact_no,
                    'start': start,
                    'end': end,
                    'date': date,
                    'time': time,
                    'content': content,
                })
                message = f"Name: {name}\nAge:{age}\nEmail: {email}\nAddress:{address}\nContact_no:{contact_no}\nStart:{start}\nEnd:{end}\nDate:{date}\nTime:{time}\nContent:{content}"
                email_msg = EmailMessage(
                    subject="Booking Details",
                    body=message,
                    from_email='vinoth@market-intellect.com',
                    to=[email],
                    reply_to=[email])
                email_msg.send()

                # send_mail('Booking Details', 'This is the message', 'sanjaikumar@market-intellect.com',
                #           ['janavinoth2000@gmail.com'], html_message=html)
                return redirect("/thank")



        else:
            form = contactform()
            return render(request, 'onlinebus/index.html', {'form': form})



