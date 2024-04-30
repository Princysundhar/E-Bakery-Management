"""E_Bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.log),
    path('login_post',views.login_post),
    path('logout',views.logout),
    path('forgot_password',views.forgot_password),
    path('forgot_password_post',views.forgot_password_post),
    path('admin_home',views.admin_home),
    path('add_category',views.add_category),
    path('add_category_post',views.add_category_post),
    path('view_category',views.view_category),
    path('delete_category/<id>',views.delete_category),
    path('add_product',views.add_product),
    path('add_product_post',views.add_product_post),
    path('view_product',views.view_product),
    path('edit_product/<id>',views.edit_product),
    path('edit_product_post/<id>',views.edit_product_post),
    path('delete_product/<id>',views.delete_product),
    path('view_user',views.view_user),
    path('change_password',views.change_password),
    path('change_password_post',views.change_password_post),
    path('view_complaint',views.view_complaint),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_feedback',views.view_feedback),
    path('view_request_from_user',views.view_request_from_user),
    path('accept_request/<id>',views.accept_request),
    path('reject_request/<id>',views.reject_request),
    path('view_verified_request',views.view_verified_request),
    path('view_payment_report',views.view_payment_report),

# ==================================================================================

    path('user_home',views.user_home),
    path('user_register',views.user_register),
    path('user_register_post',views.user_register_post),
    path('view_profile',views.view_profile),
    path('user_view_category',views.user_view_category),
    path('user_change_password',views.user_change_password),
    path('user_change_password_post',views.user_change_password_post),
    path('user_view_product/<id>',views.user_view_product),
    # path('send_request/<id>',views.send_request),
    path('send_complaint',views.send_complaint),
    path('send_complaint_post',views.send_complaint_post),
    path('send_feedback',views.send_feedback),
    path('send_feedback_post',views.send_feedback_post),
    path('view_reply',views.view_reply),
    path('add_to_cart/<id>',views.add_to_cart),
    path('add_to_cart_post/<id>',views.add_to_cart_post),
    path('view_cart',views.view_cart),
    path('place_order/<id>',views.place_order),
    path('view_order',views.view_order),
    path('cancel_order/<id>',views.cancel_order),
    path('payment_mode/<rid>',views.payment_mode),
    path('payment_mode_post/<rid>',views.payment_mode_post),
    # path('user_pay_proceed/<id>',views.user_pay_proceed),
    path('on_payment_success/<id>',views.on_payment_success),
    path('view_purchase_history',views.view_purchase_history),

]
