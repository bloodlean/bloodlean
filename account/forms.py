from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)    

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'icon', 'about']
        help_texts = {
            'username': None,
        }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords do not match")
        return cd['password2']