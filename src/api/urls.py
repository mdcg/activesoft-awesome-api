from django.urls import path

from api.views.users.authentication_views import SignInView, SignUpView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),
]
