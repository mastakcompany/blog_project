from django.views.generic import DetailView, UpdateView
from users_app.models import Profile


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
    fields = ['bio', 'social_link']
    template_name = 'users/profile_update.html'

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(
            user=self.request.user
        )
        return profile
