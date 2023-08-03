from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView

from retro_cars.review.forms import ReviewForm
from retro_cars.review.models import Review


class ReviewView(LoginRequiredMixin, FormView):
    template_name = 'reviews/reviews.html'
    form_class = ReviewForm
    success_url = reverse_lazy('review page')

    def form_valid(self, form):
        comment = form.cleaned_data['comment']
        Review.objects.create(user=self.request.user, comment=comment)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context


class DeleteReviewView(DeleteView):
    template_name = 'reviews/reviews.html'
    model = Review
    success_url = reverse_lazy('review page')
    login_url = reverse_lazy('profile login')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()

    def handle_no_permission(self):
        return HttpResponseRedirect(self.login_url)

    def post(self, request, *args, **kwargs):
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
