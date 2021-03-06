"""FotografPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import Human
from home import views
from Human.views import addcomment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('',include('home.urls')),
    path('human/',include('Human.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('user/',include('user.urls')),
    path('content/',include('content.urls')),

    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('referanslarimiz/', views.referanslarimiz, name='referanslarimiz'),
    path('error/', views.error, name='error'),

    path('categories/<int:id>/<slug:slug>/',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('content/<int:id>/<slug:slug>/',views.content_detail,name='content_detail'),
    path('menu/<int:id>',views.menu,name='menu'),

    path('search/',views.product_search,name='product_search'),
    path('search_auto/',views.product_search_auto,name='product_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('sss/', views.faq, name='faq'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
