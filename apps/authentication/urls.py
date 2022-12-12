from django.urls import path, re_path, include
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.jwt_auth import get_refresh_view

from rest_framework_simplejwt.views import TokenVerifyView

from .views import RefreshTokenView

# setting app_name and namespace in core/urls.py will cause a ReverseMatch Exception,
# django_rest_auth source needs to be altered to add a reverse match app name like so: auth:account_confirmation_email in order to work
#app_name = 'auth'

urlpatterns = [

     path('password-reset/', PasswordResetView.as_view()),
     path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

     path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
     path('register/', RegisterView.as_view()),
     path('login/', LoginView.as_view()),
     path('logout/', LogoutView.as_view()),

     path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
     path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
     
     path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
     path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
     re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),



]


