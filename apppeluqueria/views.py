from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import jefe, categoria, servicio, trabajador, cliente, hora, fechaTrabajador, reserva, fecha, galeria
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
from .forms import CreateUserForm,UpdateClientForm,UpdateUserForm,UpdateWorkerForm,UpdateBossForm, PickyAuthenticationForm, CreateCategoryForm, CreateServiceForm, CreateFechaForm, CreateHorasForm, CreateGaleriaForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordResetForm, PasswordChangeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import PasswordResetConfirmView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.views import generic
from . import views
from django.contrib import messages
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from datetime import date, time, datetime

def home(request):
    servicios = servicio.objects.all()
    categorias = categoria.objects.all()
    fotos = galeria.objects.all()
    form = PickyAuthenticationForm()
    form1 = CreateUserForm()
    form2 = PasswordResetForm()
    

    if request.method == "POST":
        if request.POST['iniciar_sesion'] == 'iniciar_sesion':
            username = request.POST['username']
            password = request.POST['password']
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                form.cleaned_data['username']
                form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('index')
            else:
                messages.error(request,_('Please enter a correct username and password. Consider that both fields are sensitive to capitalization.'))


        elif request.POST['iniciar_sesion'] == 'registrarse':
            form1 = CreateUserForm(request.POST)
            if form1.is_valid():
                username = form1.cleaned_data['username']
                form1.cleaned_data['email']
                form1.cleaned_data['phone']
                password=form1.cleaned_data['password1']
                messages.success(request,f'Usuario {username} creado')
                user = form1.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                if user.is_authenticated:
                    profile = cliente(usuario = request.user,phone = request.POST['phone'])
                    profile.save()
                    my_group = Group.objects.get(name='clientes') 
                    my_group.user_set.add(request.user)


        elif request.POST['iniciar_sesion'] == 'recuperar':
            form2 = PasswordResetForm(request.POST or None)
            if form2.is_valid():
                form2.cleaned_data['email']
                form2.save(from_email='samuelgarciamapriv@gmail.com',email_template_name= 'registration/password_reset_email_final.html', request=request)
                return redirect('reset_password_sent/')
           
    return render(request,'home.html',context= {'form':form,'form1':form1,'form2':form2,'galeria':fotos,'servicios':servicios,'categorias':categorias})

def is_member_jefe(user):
    return user.groups.filter(name='jefes').exists()

def is_member_cliente(user):
    return user.groups.filter(name='clientes').exists()

def is_member_trabajador(user):
    return user.groups.filter(name='trabajadores').exists()

def logout_view(request):
    logout(request)
    redirect('index')

def index(request):
    form = PickyAuthenticationForm()
    form1 = CreateUserForm()
    form2 = PasswordResetForm()

    if request.method == "POST":
        if request.POST['iniciar_sesion'] == 'iniciar_sesion':
            username = request.POST['username']
            password = request.POST['password']
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                form.cleaned_data['username']
                form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('index')
            else:
                messages.error(request,_('Please enter a correct username and password. Consider that both fields are sensitive to capitalization.'))


        elif request.POST['iniciar_sesion'] == 'registrarse':
            form1 = CreateUserForm(request.POST)
            if form1.is_valid():
                username = form1.cleaned_data['username']
                form1.cleaned_data['email']
                form1.cleaned_data['phone']
                password=form1.cleaned_data['password1']
                messages.success(request,f'Usuario {username} creado')
                user = form1.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                if user.is_authenticated:
                    profile = cliente(usuario = request.user,phone = request.POST['phone'])
                    profile.save()
                    my_group = Group.objects.get(name='clientes') 
                    my_group.user_set.add(request.user)


        elif request.POST['iniciar_sesion'] == 'recuperar':
            form2 = PasswordResetForm(request.POST or None)
            if form2.is_valid():
                form2.cleaned_data['email']
                form2.save(from_email='samuelgarciamapriv@gmail.com',email_template_name= 'registration/password_reset_email_final.html', request=request)
                return redirect('reset_password_sent/')

    if request.user.is_authenticated:
        if is_member_jefe(request.user):
            return redirect('boss')
        elif is_member_trabajador(request.user):
            return redirect('worker')
        elif is_member_cliente(request.user):
            return redirect('client')
           
    return render(request,'registration/login.html',context= {'form':form,'form1':form1,'form2':form2})

@permission_required('auth.is_trabajador', raise_exception=True)
def galeriaList(request):
    form = CreateGaleriaForm()
    imagenes = galeria.objects.all()
    if request.method == "POST":
        if request.POST.get('imgDelete') != None:
            imgn = galeria.objects.get(nombre_foto=request.POST['imgDelete'])
            imgn.delete()
        else:
            form = CreateGaleriaForm(request.POST)
            if form.is_valid():
                form = form.save()

    imagens = imagenes
    paginator = Paginator(imagens, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render( request ,'others/galeria-list.html', context = {'form':form,'imagenes':page_obj})


@permission_required('auth.is_boss', raise_exception=True)
def boss(request):
    from .models import fecha
    today = date.today()
    form = CreateFechaForm()
    reservas = reserva.objects.all()
    trabajadores = trabajador.objects.all()
    servicios = servicio.objects.all()
    horas = hora.objects.all()
    clientes = cliente.objects.all()
    fechaTrabajadores = fechaTrabajador.objects.all()
    fecha = fecha.objects.all()
    if request.method == "POST":
        if 'borrarReserva' in request.POST:
            borrarReserva = request.POST['borrarReserva']
            for rese in reservas:
                if borrarReserva in rese.__str__():
                    rese.delete()
                    reservas = reserva.objects.all()
                
        else:
            for hor in horas:
                if str(request.POST['horas'])==str(hor):
                    fec = request.POST['fecha'].split('-')
                    fec = fec[2]+'/'+fec[1]+'/'+fec[0]
                    reser = CreateFechaForm({'dia':fec, 'hora':hor.id})
                    if reser.is_valid():
                        reser = reser.save()
                    for tra in trabajadores:
                        if str(request.POST['trabajador'])==str(tra):
                            fetra = fechaTrabajador.objects.create(fecha = reser , peluquero = tra)
                            for ser in servicios:
                                if str(request.POST['match'])==str(ser):
                                    partesCli = request.POST['cliente'].split(' - ')
                                    for cli in clientes:
                                        if str(cli) == str(partesCli[1]):
                                            reserva.objects.create(servicio = ser, cliente = cli, fechaTrabajador = fetra)
                                            
                                            form = CreateFechaForm()

    return render( request ,'roles/boss.html', context = {'today':today.strftime("%Y-%m-%d"),'form':form,'fechas':fecha,'reservas':reservas,'clientes':clientes,'trabajadores':trabajadores,'servicios':servicios,'horas':horas,'fechaTrabajadores':fechaTrabajadores})

@permission_required('auth.is_trabajador', raise_exception=True)
def worker(request):
    from .models import fecha
    today = date.today()
    form = CreateFechaForm()
    reservas = reserva.objects.all()
    trabajadores = trabajador.objects.all()
    servicios = servicio.objects.all()
    horas = hora.objects.all()
    clientes = cliente.objects.all()
    fechaTrabajadores = fechaTrabajador.objects.all()
    fecha = fecha.objects.all()
    if request.method == "POST":
        if 'borrarReserva' in request.POST:
            borrarReserva = request.POST['borrarReserva']
            for rese in reservas:
                if borrarReserva in rese.__str__():
                    rese.delete()
                    reservas = reserva.objects.all()
                
        else:
            for hor in horas:
                if str(request.POST['horas'])==str(hor):
                    fec = request.POST['fecha'].split('-')
                    fec = fec[2]+'/'+fec[1]+'/'+fec[0]
                    reser = CreateFechaForm({'dia':fec, 'hora':hor.id})
                    if reser.is_valid():
                        reser = reser.save()
                    for tra in trabajadores:
                        if str(request.POST['trabajador'])==str(tra):
                            fetra = fechaTrabajador.objects.create(fecha = reser , peluquero = tra)
                            for ser in servicios:
                                if str(request.POST['match'])==str(ser):
                                    partesCli = request.POST['cliente'].split(' - ')
                                    for cli in clientes:
                                        if str(cli) == str(partesCli[1]):
                                            reserva.objects.create(servicio = ser, cliente = cli, fechaTrabajador = fetra)

    return render( request ,'roles/trabajador.html', context = {'today':today.strftime("%Y-%m-%d"),'form':form,'fechas':fecha,'reservas':reservas,'clientes':clientes,'trabajadores':trabajadores,'servicios':servicios,'horas':horas,'fechaTrabajadores':fechaTrabajadores})

@permission_required('auth.is_cliente', raise_exception=True)
def client(request):
    from .models import fecha
    today = date.today()
    form = CreateFechaForm()
    reservas = reserva.objects.all()
    trabajadores = trabajador.objects.all()
    servicios = servicio.objects.all()
    horas = hora.objects.all()
    clientes = cliente.objects.all()
    fechaTrabajadores = fechaTrabajador.objects.all()
    fecha = fecha.objects.all()
    if request.method == "POST":
        if 'borrarReserva' in request.POST:
            borrarReserva = request.POST['borrarReserva']
            for rese in reservas:
                if borrarReserva in rese.__str__():
                    rese.delete()
                    reservas = reserva.objects.all()
                
        else:
            for hor in horas:
                if str(request.POST['horas'])==str(hor):
                    fec = request.POST['fecha'].split('-')
                    fec = fec[2]+'/'+fec[1]+'/'+fec[0]
                    reser = CreateFechaForm({'dia':fec, 'hora':hor.id})
                    if reser.is_valid():
                        reser = reser.save()
                    for tra in trabajadores:
                        if str(request.POST['trabajador'])==str(tra):
                            fetra = fechaTrabajador.objects.create(fecha = reser , peluquero = tra)
                            for ser in servicios:
                                if str(request.POST['match'])==str(ser):
                                    partesCli = request.POST['cliente'].split(' - ')
                                    for cli in clientes:
                                        if str(cli) == str(partesCli[1]):
                                            reserva.objects.create(servicio = ser, cliente = cli, fechaTrabajador = fetra)

    return render( request ,'roles/cliente.html', context = {'today':today.strftime("%Y-%m-%d"),'form':form,'fechas':fecha,'reservas':reservas,'clientes':clientes,'trabajadores':trabajadores,'servicios':servicios,'horas':horas,'fechaTrabajadores':fechaTrabajadores})

@permission_required('auth.is_cliente', raise_exception=True)
def UserForm(request,pk):
    user = User.objects.get(username=pk)
    objs = User.objects.filter(username = pk)
    profile = None
    if is_member_jefe(user):
        profile = get_object_or_404(jefe,usuario_id = objs[0].id)
    elif is_member_cliente(user):
        profile = get_object_or_404(cliente,usuario_id = objs[0].id)
    elif is_member_trabajador(user):
        profile = get_object_or_404(trabajador,usuario_id = objs[0].id)

    user = get_object_or_404(User,username = user)
    form=None
    if is_member_cliente(user):
        form = UpdateClientForm(request.POST or None,instance = profile)
    elif is_member_trabajador(user):
        form = UpdateWorkerForm(request.POST or None,instance = profile)
    elif is_member_jefe(user):
        form = UpdateBossForm(request.POST or None,instance = profile)
        print(form)
    form1 = UpdateUserForm(instance = user)
    form2 = PasswordChangeForm(user)


    
    if request.method == 'POST':
        if request.POST['accion'] == '1':
            form1 = UpdateUserForm(request.POST or None,instance = user)
            if form.is_valid() and form1.is_valid() :
                form.save()
                form1.save() 
        else:
            form2 = PasswordChangeForm(request.user, request.POST or None)
            if form2.is_valid() : 
                form.save()
                form2.save()
    
    context ={'form':form,'form1':form1,'form2':form2}
    return render(request,'registration/user_form.html',context=context)


def obtener_trabajadores():
    from .models import trabajador
    trabajadores = trabajador.objects.all()
    filtrado = []
    for trabajador in trabajadores:
        obj = User.objects.filter(id = trabajador.usuario_id)
        filtrado.append(obj[0])
    return trabajadores,filtrado

def obtener_clientes():
    clientes = cliente.objects.all()
    filtrado = []
    for client in clientes:
        obj = User.objects.filter(id = client.usuario_id)
        filtrado.append(obj[0])
    return clientes,filtrado

def obtener_trabajador():
    clientes = trabajador.objects.all()
    filtrado = []
    for client in clientes:
        obj = User.objects.filter(id = client.usuario_id)
        filtrado.append(obj[0])
    return filtrado

def obtener_categorias():
    categorias= categoria.objects.all()
    return categorias

def obtener_servicios():
    servicios= servicio.objects.all()
    return servicios



@permission_required('auth.is_trabajador', raise_exception=True)
def userDelete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(username=pk)
        user.delete()
        return render(request, 'others/clients_list.html',context = {'clientes':obtener_clientes()})
    else:
        user = User.objects.get(username=pk)
        profile = None
        if is_member_cliente(user):
            profile = cliente.objects.get(usuario_id=user.id)
        elif is_member_trabajador(user):
            profile = trabajador.objects.get(usuario_id=user.id)
        elif is_member_jefe(user):
            profile = jefe.objects.get(usuario_id=user.id)
        context = { 'item':profile}
        return render(request,'registration/DeleteProfile.html',context = context)

@permission_required('auth.is_trabajador', raise_exception=True)
def UsersListView(request):
    template_name = 'others/clients_list.html'
    form = PickyAuthenticationForm()
    form1 = CreateUserForm()
    if request.method == "POST":
        if request.POST.get('userDelete') != None:
            user = User.objects.get(username=request.POST['userDelete'])
            user.delete()
        else: 
            form1 = CreateUserForm(request.POST)
            if form1.is_valid():
                username = form1.cleaned_data['username']
                form1.cleaned_data['email']
                form1.cleaned_data['phone']
                password=form1.cleaned_data['password1']
                messages.success(request,f'Usuario {username} creado')
                user = form1.save()
                user = authenticate(username=username, password=password)
                if user.is_authenticated:
                    profile = cliente(usuario = user,phone = request.POST['phone'])
                    profile.save()
                    my_group = Group.objects.get(name='clientes') 
                    my_group.user_set.add(user)

    clientes,users = obtener_clientes()
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,template_name,{'clientes':page_obj,'users':users,'form4':form,'form5':form1})

def HorasListView(request):
    template_name = 'others/horasList.html'
    form = CreateHorasForm()
    horas = hora.objects.all()
    if request.method == "POST":
        if request.POST.get('hourDelete') != None:
            for ho in horas:
                if str(ho) == str(request.POST['hourDelete']):
                    hor = hora.objects.get(id=ho.id)
                    hor.delete()
        else:    
            form = CreateHorasForm(request.POST)
            if form.is_valid():
                form = form.save()
    paginator = Paginator(horas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,template_name,{'horas':page_obj,'form':form})

@permission_required('auth.is_jefe', raise_exception=True)
def ClientUpdate(request,pk):
    user = User.objects.get(username=pk)
    objs = User.objects.filter(username = pk)
    profile = None
    if is_member_cliente(user):
        profile = get_object_or_404(cliente,usuario_id = objs[0].id)
    elif is_member_trabajador(user):
        profile = get_object_or_404(trabajador,usuario_id = objs[0].id)
    elif is_member_jefe(user):
        profile = get_object_or_404(jefe,usuario_id = objs[0].id)
    user = get_object_or_404(User,username = user)
    form=None
    if is_member_cliente(user):
        form = UpdateClientForm(request.POST or None,instance = profile)
    elif is_member_trabajador(user):
        form = UpdateWorkerForm(request.POST or None,instance = profile)
    elif is_member_jefe(user):
        form = UpdateBossForm(request.POST or None,instance = profile)
        print(form)
    form1 = UpdateUserForm(instance = user)
    form2 = PasswordChangeForm(user)


    
    if request.method == 'POST':
        if request.POST['accion'] == '1':
            form1 = UpdateUserForm(request.POST or None,instance = user)
            if form.is_valid() and form1.is_valid() :
                form.save()
                form1.save() 

                template_name = 'others/clients_list.html'
                form = PickyAuthenticationForm()
                form1 = CreateUserForm()
                clientes,users = obtener_clientes()
                paginator = Paginator(clientes, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,template_name,{'clientes':page_obj,'users':users,'form4':form,'form5':form1})
        else:
            form2 = PasswordChangeForm(request.user, request.POST or None)
            if form2.is_valid() : 
                form.save()
                form2.save()

                template_name = 'others/clients_list.html'
                form = PickyAuthenticationForm()
                form1 = CreateUserForm()
                clientes,users = obtener_clientes()
                paginator = Paginator(clientes, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,template_name,{'clientes':page_obj,'users':users,'form4':form,'form5':form1})
    
    context ={'form':form,'form1':form1,'form2':form2}
    return render(request,'registration/user_form.html',context=context)

@permission_required('auth.is_jefe', raise_exception=True)
def WorkersListView(request):
    template_name = 'others/workers_list.html'
    form = PickyAuthenticationForm()
    form1 = CreateUserForm()
    if request.method == "POST":
        if request.POST.get('userDelete') != None:
            user = User.objects.get(username=request.POST['userDelete'])
            user.delete()
        else: 
            form1 = CreateUserForm(request.POST)
            if form1.is_valid():
                username = form1.cleaned_data['username']
                form1.cleaned_data['email']
                form1.cleaned_data['phone']
                password=form1.cleaned_data['password1']
                messages.success(request,f'Usuario {username} creado')
                user = form1.save()
                user = authenticate(username=username, password=password)
                if user.is_authenticated:
                    profile = trabajador(usuario = user,phone = request.POST['phone'])
                    profile.save()
                    my_group = Group.objects.get(name='trabajadores') 
                    my_group.user_set.add(user)

    trabajadores,users = obtener_trabajadores()
    paginator = Paginator(trabajadores, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,template_name,{'trabajadores':page_obj,'users':users,'form4':form,'form5':form1})

@permission_required('auth.is_jefe', raise_exception=True)
def WorkerUpdate(request,pk):
    user = User.objects.get(username=pk)
    objs = User.objects.filter(username = pk)
    profile = None
    if is_member_cliente(user):
        profile = get_object_or_404(cliente,usuario_id = objs[0].id)
    elif is_member_trabajador(user):
        profile = get_object_or_404(trabajador,usuario_id = objs[0].id)
    elif is_member_jefe(user):
        profile = get_object_or_404(jefe,usuario_id = objs[0].id)
    user = get_object_or_404(User,username = user)
    form=None
    if is_member_cliente(user):
        form = UpdateClientForm(request.POST or None,instance = profile)
    elif is_member_trabajador(user):
        form = UpdateWorkerForm(request.POST or None,instance = profile)
    elif is_member_jefe(user):
        form = UpdateBossForm(request.POST or None,instance = profile)
        print(form)
    form1 = UpdateUserForm(instance = user)
    form2 = PasswordChangeForm(user)


    
    if request.method == 'POST':
        if request.POST['accion'] == '1':
            form1 = UpdateUserForm(request.POST or None,instance = user)
            if form.is_valid() and form1.is_valid() :
                form.save()
                form1.save() 

                template_name = 'others/workers_list.html'
                form = PickyAuthenticationForm()
                form1 = CreateUserForm()
                trabajadores,users = obtener_trabajadores()
                paginator = Paginator(trabajadores, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,template_name,{'trabajadores':page_obj,'users':users,'form4':form,'form5':form1})
        else:
            form2 = PasswordChangeForm(request.user, request.POST or None)
            if form2.is_valid() : 
                form.save()
                form2.save()

                template_name = 'others/workers_list.html'
                form = PickyAuthenticationForm()
                form1 = CreateUserForm()
                trabajadores,users = obtener_trabajadores()
                paginator = Paginator(trabajadores, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request,template_name,{'trabajadores':page_obj,'users':users,'form4':form,'form5':form1})
    
    context ={'form':form,'form1':form1,'form2':form2}
    return render(request,'registration/user_form.html',context=context)

def categories_services(request):
    template_name = 'others/categories_services_list.html'
    from .models import servicio,categoria
    form = CreateCategoryForm()
    form1 = CreateServiceForm()
    if request.method == 'POST':
        if request.POST.get('serviceDelete') != None:
            servicio = servicio.objects.get(id=request.POST['serviceDelete'])
            servicio.delete()
        elif request.POST.get('categoryDelete') != None:
            categoria = categoria.objects.get(id=request.POST['categoryDelete'])
            categoria.delete()
        elif request.POST['accion'] == '1':
            form = CreateCategoryForm(request.POST or None)
            if form.is_valid() : 
                form.save()
        else:
            form1 = CreateServiceForm(request.POST or None)
            if form1.is_valid() : 
                form1.save()
    return render(request,template_name,context={'form1':form1,'form':form,'categorias':obtener_categorias(),'servicios':obtener_servicios()})

class CategoryCreate(CreateView):
    model = categoria
    fields = '__all__'
    template_name = 'others/categories_services_form.html'
    permission_required = 'auth.is_trabajador'

class CategoryUpdate(UpdateView):
    model = categoria
    fields = '__all__'
    template_name = 'others/categories_services_form.html'
    permission_required = 'auth.is_jefe'

class CategoryDelete(DeleteView):
    model = categoria
    fields = '__all__'
    template_name = 'others/category_confirm_delete_form.html'
    permission_required = 'auth.is_jefe'

class ServicioCreate(CreateView):
    model = servicio
    fields = '__all__'
    template_name = 'others/categories_services_form.html'
    permission_required = 'auth.is_trabajador'
    

class ServicioUpdate(UpdateView):
    model = servicio
    fields = '__all__'
    template_name = 'others/categories_services_form.html'
    permission_required = 'auth.is_jefe'

class ServicioDelete(DeleteView):
    model = servicio
    fields = '__all__'
    template_name = 'others/service_confirm_delete_form.html'
    permission_required = 'auth.is_jefe'

@permission_required('auth.is_jefe', raise_exception=True)
def ClientCreate(request):
    if  request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            profile = cliente(usuario = User.objects.get(username=request.POST['username']),phone = request.POST['phone'])
            profile.save()
        return render( request ,'others/clients_list.html', context = {'clientes':obtener_clientes()})
    else:
        context={'form': CreateUserForm()}
        return render( request ,'others/clients_create.html', context = context)