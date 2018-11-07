from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView


# Custom user model
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """Detail view for the user model."""

    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'users/user_detail.html'


class UserListView(LoginRequiredMixin, ListView):
    """List view for the user model."""

    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'users/user_list.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Update view for the user model."""

    model = User
    fields = ['name']
    template_name = 'users/user_form.html'

    def get_success_url(self):
        return reverse('accounts:user-detail')

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """Redirect view for the user model."""

    permanent = False

    def get_redirect_url(self):
        return reverse('showcase:demo')


# View functions
user_detail_view = UserDetailView.as_view()
user_list_view = UserListView.as_view()
user_update_view = UserUpdateView.as_view()
user_redirect_view = UserRedirectView.as_view()
