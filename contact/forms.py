from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
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

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'class-a class-b',
        #     'placeholder': 'Primeiro Nome',
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )
        # Pode mexer do widgets aqui, no __init__ ou criar uma classe própria!
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class-a class-b',
        #             'placeholder': 'Escreva seu primeiro nome'
        #         }
        #     )
        # }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError(
                'MENSAGEM DE ERRO',
                code='invalid'
            )
        )
        return super().clean()