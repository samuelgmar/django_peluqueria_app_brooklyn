from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import cliente, trabajador, jefe, categoria, servicio, fecha, hora, galeria
from django import forms
from django.core.validators import RegexValidator
from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

class CreateUserForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("The phone number should be entered in the format: '+999999999'. Up to 15 digits are allowed."))
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    error_messages = {
        'password_mismatch': _("The two password fields do not match."),
    }
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','phone']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


class PickyAuthenticationForm(AuthenticationForm):
    pass

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'

class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = '__all__'

class CreateFechaForm(forms.ModelForm):
    class Meta:
        model = fecha
        fields = '__all__'

class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['phone']

class CreateHorasForm(forms.ModelForm):
    class Meta:
        model = hora
        fields = '__all__'

class CreateGaleriaForm(forms.ModelForm):
    class Meta:
        model = galeria
        fields = '__all__'

class UpdateWorkerForm(forms.ModelForm):
    class Meta:
        model = trabajador
        fields = ['phone']

class UpdateBossForm(forms.ModelForm):
    class Meta:
        model = jefe
        fields = ['phone']
    
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'




