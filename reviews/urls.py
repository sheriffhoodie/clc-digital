from django.urls import path, include
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewList.as_view(template_name='review_list.html'), name="all"),
    path('new/', views.CreateReview.as_view(template_name='review_form.html'), name="create"),
]
