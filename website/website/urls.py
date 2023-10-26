"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import *
from cart.views import *
from buynow.views import *
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('cart/', cart, name="cart"),
    path('buynow/', buynow, name="buynow"),
    path('successful/', successful, name="successful"),
    path('productcard/', productcard, name="productcard"),
    path('updateItem/', updateItem, name="updateItem"),
    path('productview/<int:myid>', productview, name="productview"),
     path('signup/', signupage,name="signup"),
    path('login/',login,name="login"),
    path('logout/',Logoutpage,name="logout")
#    path('add_to_cart/', home.add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
