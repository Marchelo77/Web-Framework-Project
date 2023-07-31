from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from retro_cars.cars.forms import CarCreateForm, CarEditForm
from retro_cars.cars.models import RetroCar


class CarPageView(ListView):
    template_name = 'cars/cars.html'
    model = RetroCar
    context_object_name = 'cars'


class DetailCarView(DetailView):
    template_name = 'cars/car-details.html'
    model = RetroCar
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class CarCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cars/car-create.html'
    form_class = CarCreateForm

    def get_success_url(self):
        return reverse('car page')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class EditCarView(UpdateView):
    model = RetroCar
    form_class = CarEditForm
    template_name = 'cars/car-edit.html'

    def get_success_url(self):
        return reverse('car details', kwargs={
            'pk': self.object.pk
        })


class DeleteCarView(DeleteView):
    model = RetroCar
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('car page')
