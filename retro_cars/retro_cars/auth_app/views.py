from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

from retro_cars.auth_app.forms import RegisterUserForm, LoginUserForm, AppUserEditForm

UserModel = get_user_model()


class OnlyAnonymousUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_authenticated_user(request)
        return super().dispatch(request, *args, **kwargs)

    def handle_authenticated_user(self, request):
        return HttpResponseRedirect(reverse('home_page'))


class ProfileDetailsView(views.DetailView):
    template_name = 'profile/profile.html'
    model = UserModel


class RegisterUserView(OnlyAnonymousUserMixin, views.CreateView):
    model = UserModel
    form_class = RegisterUserForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):

        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def form_invalid(self, form):

        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):

        return self.request.GET.get('next', self.success_url)


class LoginUserView(OnlyAnonymousUserMixin, auth_views.LoginView):
    template_name = 'profile/profile-login.html'
    form_class = LoginUserForm


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = AppUserEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile page', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home_page')
