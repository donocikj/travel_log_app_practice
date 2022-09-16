from django.urls import path
from tlog.views import test_view

urlpatterns = [
    path('', test_view, name='test_view'),
]
