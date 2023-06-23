from django.contrib import admin
from django.urls import path
from attendance.views import my_form_view , success , data_list_view , deregister_item_view , scan_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_list_view, name='data_list'),
    path('register/', my_form_view, name='my_form'),
    path('success/', success, name='success'),
    path('deregister/', deregister_item_view, name='deregister_item'),
    path('scan/',   scan_view, name='scan'),
]
