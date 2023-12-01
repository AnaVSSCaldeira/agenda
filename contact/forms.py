from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
            
        )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class': 'class-a class-b',
            'placeholder': 'Escreva seu Primeiro Nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuário',
    )
    
    def clean(self): #Pode fazer a validação deste jeito
        cleaned_data = self.cleaned_data
        
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        error = ValidationError(
                    'Primeiro nome e segundo nome não podem ser iguais!',
                    code='invalid'
                )

        if first_name == last_name:
            self.add_error('first_name', error)
            self.add_error('last_name', error)

        return super().clean()
    
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(
        required=True,
        min_length=3,
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já possui um usuário cadastrado com este email',
                    code='invalid'
                )
            )

        return email