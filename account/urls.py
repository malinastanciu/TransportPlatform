from django.contrib.auth import views as auth_views
from django.urls import path
from account import views as account_views

urlpatterns = [
    path('register/', account_views.registerPage, name='register'),
    path('login/', account_views.loginPage, name='login'),
    path('logout/', account_views.logoutPage, name='logout'),
    path('reset-password/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name="password_reset"),
    path('reset-password-done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('reset-password-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name="password_reset_complete"),
    path('account/change-password/', auth_views.PasswordChangeView.as_view(
         template_name='account/change_password.html'),
         name='change_password'),
    path('account/change-password-done/',auth_views.PasswordChangeDoneView.as_view(
        template_name='account/change_password_done.html'),
         name='password_change_done'),
]
