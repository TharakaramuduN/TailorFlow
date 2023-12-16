"""
URL configuration for TailorFlow project.

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
from django.conf import settings
from . import views

urlpatterns = [
    path('api/check-email-exists/<int:customer_id>/', views.check_email_exists,
         name='check_email_exists'),
    path('api/check-phone-exists/<int:customer_id>/', views.check_phone_exists,
         name='check_phone_exists'),
    path("base/", views.base_view, name="base"),
    path("", views.home_view, name="home"),
    path('admin/', admin.site.urls),
    path('newCustomer1/', views.new_customer1, name="newCustomer"),
    path('customers/', views.customers, name='Customers'),
    path('customer/<int:customer_id>/measurements/',
         views.customer_measurements, name='CustomerMeasurements'),
    path('edit-customer/<int:customer_id>/details/',
         views.edit_customers, name='edit_customers'),
    path('orders/', views.orders, name="orders"),
    path('add-products/<int:customer_id>/',
         views.add_products, name='add-products'),
    path('delete-customer/<int:customer_id>',
         views.delete_customer, name="delete-customer"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
