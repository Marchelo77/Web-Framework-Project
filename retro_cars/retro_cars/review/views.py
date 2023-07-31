from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DeleteView, FormView

from retro_cars.review.forms import ReviewForm
from retro_cars.review.models import Review


class ReviewView(FormView):
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

    def get_object(self, queryset=None):
        # Get the review object to be deleted
        obj = super().get_object(queryset=queryset)

        return obj

    def post(self, request, *args, **kwargs):
        # Call the delete() method to delete the review
        self.object = self.get_object()
        self.object.delete()

        # Redirect to the success_url after the deletion
        return HttpResponseRedirect(self.get_success_url())
