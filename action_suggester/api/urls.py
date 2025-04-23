from django.urls import path
from .views import AnalyzeView
# converts the class-based view into a callable function that Django can use to handle requests.
urlpatterns = [
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
]

