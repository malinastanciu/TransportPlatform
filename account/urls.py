from django.contrib.auth import views as auth_views
from django.urls import path
from account import views as account_views

urlpatterns = [
    path('register/', account_views.registerPage, name='register'),
    path('login/', account_views.loginPage, name='login'),
    path('logout/', account_views.logoutPage, name='logout'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name="password_reset"),
    path('reset_password_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name="password_reset_complete"),
]
