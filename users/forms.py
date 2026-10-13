from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm


class MarketplaceAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Foydalanuvchi nomi'
        self.fields['password'].label = 'Parol'


class UzbekPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Amaldagi parol'
        self.fields['new_password1'].label = 'Yangi parol'
        self.fields['new_password2'].label = 'Yangi parolni tasdiqlang'

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Ism'
        self.fields['username'].label = 'Foydalanuvchi nomi'
        self.fields['email'].label = 'Elektron pochta'
        self.fields['password1'].label = 'Parol'
        self.fields['password2'].label = 'Parolni tasdiqlang'

    class Meta:
        model = CustomUser
        fields = ('first_name', 'username', 'email')
        
class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Ism'
        self.fields['last_name'].label = 'Familiya'
        self.fields['username'].label = 'Foydalanuvchi nomi'
        self.fields['email'].label = 'Elektron pochta'
        self.fields['tg_username'].label = 'Telegram foydalanuvchi nomi'
        self.fields['phone_number'].label = 'Telefon raqami'
        self.fields['avatar'].label = 'Profil rasmi'

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", 'email', "tg_username", 'phone_number', 'avatar')
            