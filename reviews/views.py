from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms

class ReviewList(generic.ListView):
    model = models.Review

class CreateReview(LoginRequiredMixin, generic.CreateView):
    model = models.Review
    fields = ('title', 'body', 'rating')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
