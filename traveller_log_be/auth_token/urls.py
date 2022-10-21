from django.urls import path
from auth_token.views import user_update_view, login_view, auth_view, logout_view

urlpatterns = [
    path('users/', user_update_view, name='users update view'),
    path('login/', login_view, name='login view' ),
    path('logout/', logout_view, name='logout_view' ),
    path('', auth_view, name='auth_view' )
]
