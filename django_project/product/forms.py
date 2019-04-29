from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ID'
    }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mt-2',
            'placeholder': 'password'
        }))
