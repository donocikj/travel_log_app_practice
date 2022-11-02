from django.urls import path
from tlog.views import entries_list_view, entry_individual_view, test_view, travels_list_view, travel_individual_view

urlpatterns = [
    path('', test_view, name='test_view'),
    path('entries/<int:id>/', entry_individual_view, name='entries_individual_view'),
    path('entries/', entries_list_view, name='entries_list_view'),
    path('travels/<int:id>/', travel_individual_view, name='travels_individual_view'),
    path('travels/', travels_list_view, name='travels_list_view'),
]
