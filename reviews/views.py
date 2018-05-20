from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
# from . import forms

class ReviewList(generic.ListView):
    model = models.Review
