from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from . import views
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name='index'),
    path('boss/', login_required(views.boss), name='boss'),
    path('worker/', login_required(views.worker), name='worker'),
    path('client/', login_required(views.client), name='client'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_form_final.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_done_final.html"), name ='password_reset_complete'),
    path('accounts/logout/',login_required(views.logout),name='logout'),
    
    path('horas/', login_required(views.HorasListView), name='horas'),
    path('galeria/', login_required(views.galeriaList), name='galeria'),

    path('users/', login_required(views.UsersListView), name='users'),
    path('user/update/<pk>', login_required(views.UserForm), name='user_update'),
    
    path('client/update/<pk>', login_required(views.ClientUpdate), name='client_update'),

    path('workers/', login_required(views.WorkersListView), name='workers'),
    path('worker/update/<pk>', login_required(views.WorkerUpdate), name='worker_update'),
    
    path('categories/', login_required(views.categories_services), name='categories'),
    
    path('category/create/', login_required(views.CategoryCreate.as_view()), name='category_create'),
    path('category/update/<pk>', login_required(views.CategoryUpdate.as_view(success_url="/peluqueria/categories")), name='category_update'),
    path('category/delete/<pk>', login_required(views.CategoryDelete.as_view(success_url="/peluqueria/categories")), name='category_delete'),
    
    path('service/create/', login_required(views.ServicioCreate.as_view(success_url="/peluqueria/categories")), name='service_create'),
    path('service/update/<pk>', login_required(views.ServicioUpdate.as_view(success_url="/peluqueria/categories")), name='service_update'),
    path('service/delete/<pk>', login_required(views.ServicioDelete.as_view(success_url="/peluqueria/categories")), name='service_delete'),
   ]
    