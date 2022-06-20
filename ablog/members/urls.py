from django.urls import path
from .views import UserRegistrationView, UserEditView,ShowProfilePageView, EditProfilePageView, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change_password.html'))

]