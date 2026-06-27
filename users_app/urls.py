from django.urls import path
from django.urls import reverse_lazy
from users_app import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

app_name = 'users_app'

urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('edit/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'password-change/',
        PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url=reverse_lazy('users:password_change_done'),
        ),
        name='password_change',
    ),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
]
