from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password','email')
        help_texts = {
            'username': _(''),
            'password':_('')
        }
        error_messages = {
            'username': {
                'unique': _("Tакое имя уже существует"),
            },
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3 mt-3',
                                           'id': 'InputName',
                                           'placeholder': 'Имя',
                                           'pattern': '^(([А-Я A-Z]{1}[а-яa-z]+$)|([А-ЯA-Z]{1}[а-яa-z]+\s$))',
                                           'title': 'Имя с большой буквой'
                                           }),
            'email': forms.EmailInput(attrs={'class': 'form-control  mb-3 mt-3',
                                             'id': 'InputEmail',
                                             'title': 'Пожалуйста напишите корректную почту',
                                             'placeholder': 'Почта',
                                             }),

            'password': forms.PasswordInput(attrs={'class': 'form-control  mb-3 mt-3',
                                                   'id': 'InputPassword',
                                                   'placeholder': 'Пароль'
                                                   })
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email уже используется'))
        return cleaned_data



class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['lname']
        widgets = {
            'lname': forms.TextInput(attrs={'class': 'form-control mb-3 mt-3',
                                            'id': 'InputEmail',
                                            'placeholder': 'Фамиля',
                                            'pattern': '^(([А-Я A-Z]{1}[а-яa-z]+$)|([А-ЯA-Z]{1}[а-яa-z]+\s$))',
                                            'title': 'Имя с большой буквой'
                                            })
        }