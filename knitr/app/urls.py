from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DocumentListView


urlpatterns = [
    path('', DocumentListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
