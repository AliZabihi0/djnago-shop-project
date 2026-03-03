from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import AddAddressView

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='Register'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.edit_profile, name='profile'),
    path('address/add', AddAddressView.as_view(), name='add_address'),
    path('address/list', views.AddressListView.as_view(), name='list_address'),
]
