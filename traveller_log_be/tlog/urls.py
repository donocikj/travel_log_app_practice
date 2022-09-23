from django.urls import path
from tlog.views import entries_list_view, test_view, travels_list_view

urlpatterns = [
    path('', test_view, name='test_view'),
    path('entries/', entries_list_view, name='entries_list_view'),
    path('travels/', travels_list_view, name='travels_list_view'),
]
