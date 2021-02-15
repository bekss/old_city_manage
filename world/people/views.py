from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Sultan, Vazir, Rysar, Soldat, Rab


class Sultan(LoginRequiredMixin, ListView):
    login_url = 'user_login'
    template_name = 'world/sultan.html'
    queryset = Sultan.objects.all()


class Vazir(LoginRequiredMixin, ListView):
    login_url = 'user_login'
    model = Vazir
    template_name = 'world/sultan.html'
    queryset = Vazir.objects.all()


class Rysar(LoginRequiredMixin, ListView):
    login_url = 'user_login'
    model = Rysar
    template_name = 'world/sultan.html'
    queryset = Rysar.objects.all()


class Soldat(LoginRequiredMixin, ListView):
    login_url = 'user_login'
    model = Soldat
    template_name = 'world/sultan.html'
    queryset = Soldat.objects.all()


class Rab(LoginRequiredMixin, ListView):
    login_url = 'user_login'
    model = Rab
    template_name = 'world/sultan.html'
    queryset = Rab.objects.all()
