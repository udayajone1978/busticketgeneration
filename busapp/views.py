# # from django.shortcuts import render,redirect,HttpResponse
#
# from django.http import JsonResponse
# from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
# from django.core.exceptions import ValidationError
# # from .forms import ContactUsForm, RegistrationFormSeller, RegistrationForm, RegistrationFormSeller2, CartForm
# from django.urls import reverse_lazy, reverse
# # from .models import SellerAdditional, CustomUser, Contact, Product, ProductInCart, Cart
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.template.loader import render_to_string
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from busproject import settings
# from django.core.mail import send_mail
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group
# # om .models import *
# # from .forms import CreateUserForm
# # from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only
# from django import forms
# # Create your views here.
# # def index(request):
# #     return render(request,"busapp/index.html")
# #
# #
# # def detail(request):
# #     return render(request,"busapp/details.html")
# #
# #
# # def empDetails(request):
# #     name="sanjai"
# #     emp_data=Driver.objects.all()
# #     emp_dict = {"emp_list":emp_data}
# #     return render(request, "busapp/index.html", context =emp_dict)
# #
# #
# # def create_view(request):
# #     form=DriverForm()
# #     if request.method =="POST":
# #         form = DriverForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect("home/")
# #     return render(request,"busapp/details.html",{"form":form})
#
# @login_required(login_url='signin')
# @admin_only
# def empDetails(request):
#     emp_data=Driver.objects.all()
#     emp_dict = {"emp_list":emp_data}
#     return render(request, "busapp/index.html", context =emp_dict)
#     #return HttpResponse("<h1 this is my application <h1>")
# @login_required(login_url='signin')
# @allowed_users(allowed_roles=['admin','Driver'])
# def driverDetails(request):
#     emp_data=Driver.objects.all()
#     emp_dict = {"emp_list":emp_data}
#     return render(request, "busapp/driver.html", context =emp_dict)
# #u
# def create_view(request):
#     form=DriverForm()
#     if request.method =="POST":
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/home")
#     return render(request,"busapp/create.html",{"form":form})
#
#
# def delete_view(request,id):
#     emp_data=Driver.objects.get(id=id)
#     emp_data.delete()
#     return redirect("/home")
#
# def update_view(request,id):
#     emp_data=Driver.objects.get(id=id)
#     # emp_data={"emp_data":emp_data}
#     # return render(request, "busapp/update.html", context=emp_data)
#     if request.method == "POST":
#         drivername=request.POST["drivername"]
#         age=request.POST["age"]
#         contact_no=request.POST["contact_no"]
#         bus_no=request.POST["bus_no"]
#         emp_data.drivername = drivername
#         emp_data.age=age
#         emp_data.contact_no=contact_no
#         emp_data.bus_no=bus_no
#         emp_data.save()
#         return redirect("/home")
#     return render(request, "busapp/update.html",{"emp_data":emp_data})
#
#
# # @login_required(login_url='login')
# # @allowed_users(allowed_roles=['customer'])
# @login_required(login_url='signin')
# @allowed_users(allowed_roles=['admin','customer'])
# def consumerdisplay_view(request):
#     info=Customer.objects.all()
#     return render(request,"busapp/consumerdisplay.html",{"info":info})
#
#
# def consumer_view(request):
#     form1=CustomerForm()
#     if request.method =='POST':
#         form1=CustomerForm(request.POST)
#         if form1.is_valid():
#             form1.save()
#             return redirect('/consumerdisplay')
#
#     return render(request,'busapp/consumeradd.html',{'form1':form1})
#
# def deleteconsumer_view(request ,id):
#     info =Customer.objects.get(id=id)
#     info.delete()
#     return redirect('/consumerdisplay')
#
# def updateconsumer_view(request, id):
#         consumer_data = Customer.objects.get(id=id)
#         if request.method == ('POST'):
#             name = request.POST["name"]
#             age= request.POST["age"]
#             address=request.POST['address']
#             phone=request.POST['phone']
#             start = request.POST["start"]
#             end = request.POST["end"]
#             date = request.POST["date"]
#             time = request.POST["time"]
#             consumer_data.name = name
#             consumer_data.age = age
#             consumer_data.address = address
#             consumer_data.phone = phone
#             consumer_data.start= start
#             consumer_data.end = end
#             consumer_data.date = date
#             consumer_data.time = time
#             consumer_data.save()
#             return redirect('/consumerdisplay')
#         return render(request, 'busapp/consumerupdate.html', {"consumer_data": consumer_data})
# def rough(request):
#     emp_data = Driver.objects.all()
#     emp_dict = {"emp_list": emp_data}
#     return render(request,"busapp/rough.html",context =emp_dict)
#
# def consumerlogin(request):
#     info = Customer.objects.all()
#     return render(request,"busapp/customerlogin.html",{"info":info})
#
# # from django.contrib.auth.models import Group
# # from django.http import HttpResponse
# # from django.contrib.auth.decorators import login_required
# #
# # @login_required
# # def addtopremiumGroup(request):
# #     group=Driver.objects.get(name="Driver")
# #     request.user.groups.add(group)
# #     return HttpResponse("successfully added")
#
# # from django.contrib.auth.decorators import group_required
# # @group_required("Driver")
# # def premiumproducts(request):
# #     if request.user.groups.filter(name="premium").exist():
# #         product=Driver.objects.all()
# from django.contrib.auth.models import User,auth,UserManager
# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login
# from django.shortcuts import get_object_or_404, render
# # def login(request,user):
# #     User=User.objects.create_user(username=username,email=email,password=password)
# #     User.last_name="lennon"
# #     User.save()
# #     user = authenticate(username='john', password='secret')
# #     if user is not None:
# #         # A backend authenticated the credentials
# #         auth.login(request,user)
# #         return redirect("/home")
# #     else:
# #         messages.info(request, "invalid user")
# #         return render(request, "busapp/login.html")
# #         # No backend authenticated the credentials
#
#
# from .form import  CreateUserForm
# def homepage(request):
#     return render(request,"busapp/homepage.html")
# # @unauthenticated_user
# def signup(request):
#     # context = {}
#     # if request.method == 'POST':
#     #     name = request.POST.get('name')
#     #     email = request.POST.get('email')
#     #     password = request.POST.get('password')
#     #     user = User.objects.create_user(username=name,email=email,password=password,)
#     #     # if User.objects.filter(email=email):
#     #     #     context["error"] = "Provide valid credentials"
#     #     #     return render(request, 'busapp/signup.html', context)
#     #     if user:
#     #         login(request,user)
#     #         return render(request,'busapp/thank.html')
#     #     else:
#     #         context["error"] = "Provide valid credentials"
#     #         return render(request, 'busapp/signup.html', context)
#     # else:
#     #     return render(request, 'busapp/signup.html', context)
#     form2 = CreateUserForm()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = User.objects.create_user(username=name, email=email, password=password, )
#         form2 = CreateUserForm(request.POST)
#         if user:
#             login(request,user)
#             return render(request,'busapp/thank.html')
#             username = form2.cleaned_data.get('username')
#
#             group = Group.objects.get(name='customer')
#             user.groups.add(group)
#
#             messages.success(request, 'Account was created for ' + username)
#
#             return redirect('signin')
#
#     context = {'form2': form2}
#     return render(request, 'busapp/signup.html', context)
#
#
# # @unauthenticated_user
# def signin(request):
#     context = {}
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         password = request.POST.get('password')
#         user = authenticate(request, username=name,password=password)
#         if user is not None:
#             login(request, user)
#             context["user"] = name
#             context["id"] = request.user.id
#             return redirect("home")
#
#         else:
#             messages.error(request, 'Username or password is incorrect')
#
#     context = {}
#     return render(request, 'busapp/signin.html', context)
#
# # else:
# #         #context["error"] = "You are not logged in"
# #
# #         return render(request, 'busapp/signin.html',context)
#
# def signout(request):
#     context = {}
#     logout(request)
#     context['error'] = "You have been logged out"
#     return render(request, 'busapp/signin.html', context)
#
#
#
# # #create group
# from django.contrib.auth.models import Group
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
#
# # @login_required()
# # def busticket(request):
# #     group=Group.objects.get(name="Driver")
# #     request.user.groups.add(group)
# #     return HttpResponse("successfullyadded")
# #
# #
# #
# # from busapp.models import User
# # from .decorators import group_required
# # @group_required("Driver")
# # def driver(request):
# #     if request.user.groups.filter(name='Driver').exists():
# #         product=Driver.objects.all()
# #         return render(request,"busapp/index.html",{"product":product})
# #     else:
# #         return HttpResponse("restricted page")
# # #
# # from .mixins import CheckPremiumGroupMixin
# # class PremiumProducts(CheckPremiumGroupMixin,ListView):
# #     template_name="busapp/index.html"
# #     model=Driver
# #     context_object_name="product"
# #     paginate_by=2
# #     permission_required = "busapp.view_premiumproduct"
#
# from django.contrib.auth.decorators import permission_required
#
#
#
#
# # def Driver1(request):
# #     if request.user.has_perm("busapp.view_Driver1"):
# #         driv=Driver.objects.all()
# #         return redirect("home")
# #         return render(request,"busapp/index.html",{"driv":driv})
# #         # if request.user.has_perm("busapp.view_Driver1"):
# #         #     cust = Customer.objects.all()
# #         #     return redirect("/consumerdisplay")
# #         #     return render(request, "busapp/consumerdisplay.html", {"cust": cust})
# #         # else:
# #         #     pass
# #
# #     else:
# #         # return HttpResponse("only admin can access this page")
# #         return redirect("consumerlogin/")
#
#         # return render(request,"busapp/driver.html")
# #
# # from django.contrib.auth.models import Permission, User
# # from django.contrib.contenttypes.models import ContentType
# # from django.shortcuts import get_object_or_404
# #
# # from busapp.models import BlogPost
#
# # def user_gains_perms(request, user_id):
# #     user = get_object_or_404(User, pk=user_id)
# #     # any permission check will cache the current set of permissions
# #     user.has_perm('busapp.change_blogpost')
# #
# #     content_type = ContentType.objects.get_for_model(BlogPost)
# #     permission = Driver.objects.get(
# #         codename='change_blogpost',
# #         content_type=content_type,
# #     )
# #     user.user_permissions.add(permission)
# #
# #     # Checking the cached permission set
# #     user.has_perm('busapp.change_blogpost')  # False
# #
# #     # Request new instance of User
# #     # Be aware that user.refresh_from_db() won't clear the cache.
# #     user = get_object_or_404(User, pk=user_id)
# #
# #     # Permission cache is repopulated from the database
# #     user.has_perm('busapp.change_blogpost')  # True
# #     return render(request,"busapp/index.html")
#
# # @login_required(login_url="login")
# # def home(request):
# #     driv=Driver.objects.all()
# #     group=User.objects.all()
# # from django.contrib.auth.models import Group, Permission
# # from django.contrib.contenttypes.models import ContentType
# # # from api.models import Project
# # new_group,created = Group.objects.get_or_create()
# # # Code to add permission to group ???
# # ct = ContentType.objects.get_for_model(Project)
# #
# # # Now what - Say I want to add 'Can add project' permission to new_group?
# # permission = Permission.objects.create(admin="admin",
# #                                    driver='driver',
# #                                    customer='customer',)
# # new_group.permissions.add(permission)
