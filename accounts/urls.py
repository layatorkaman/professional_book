# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
# from .form import CustomUserCreationForm, CustomUserChangeForm
#
# CustomUser = get_user_model()
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', ]
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
from django.urls import path
from .views import SignupPageView
urlpatterns = [
path('signup/', SignupPageView.as_view(), name='signup')
]