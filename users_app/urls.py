from django.urls import path

from users_app import views
app_name = 'users_app'

urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('edit/', views.ProfileUpdateView.as_view(), name='profile_update'),
]
