from django.views.generic import DetailView, UpdateView
from users_app.models import Profile
from django.urls import reverse_lazy


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user
        )
        return profile


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio', 'social_link', 'avatar']
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('users:profile_detail')

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user
        )
        return profile


class RegisterView:
    pass
