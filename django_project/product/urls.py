from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.product, name='product'),
    path('<int:category_type>', views.product_type, name='product_type'),
    # path('login/',
    #      auth_views.LoginView.as_view(template_name='login.html'),
    #      name='login'),
    # path('login/', views.login, name='login'),
    # path('', views.home, name='home'),
]
