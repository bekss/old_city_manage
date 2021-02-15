from django.contrib import admin
from django.urls import path

from people.views import Sultan, Vazir, Rysar, Soldat, Rab
from town.views import register, user_login, user_logout, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user_login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('sultan/', Sultan.as_view(), name='sultan'),
    path('vazir/', Vazir.as_view(), name='vazir'),
    path('rysar/', Rysar.as_view(), name='rysar'),
    path('soldat/', Soldat.as_view(), name='soldat'),
    path('rab/', Rab.as_view(), name='rab'),
]
