"""
URL configuration for algosms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index , name='index'),
    
    path('admin_login/',views.admin_login, name='admin_login'),
    path('client_login/',views.client_login, name='client_login'),
    path('registration/',views.registration, name='registration'),
    path('logout/',views.logoutUser, name='logoutUser'),
    path('multibank/',views.multibank, name='multibank'),
    
    
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('admin_message/',views.admin_message, name='admin_message'),
    path('admin_signals/',views.admin_signals, name='admin_signals'),
    path('admin_thistory/',views.admin_thistory, name='admin_thistory'),
    path('admin_tstatus/',views.admin_tstatus, name='admin_tstatus'),
    path('admin_client/',views.admin_client,name='admin_client'),
    path('admin_help_center/',views.admin_help_center,name='admin_help_center'),
    path('admin_change_password/',views.admin_change_password,name='admin_change_password'),
    
    path('client_dashboard/',views.client_dashboard, name='client_dashboard'),
    path('client_signals/',views.client_signals, name='client_signals'),
    path('client_trade_HISTORY/',views.client_trade_HISTORY, name='client_trade_HISTORY'),
    path('client_tstatus/',views.client_tstatus, name='client_tstatus'),
    path('change_password/',views.change_password, name='change_password'),
    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
