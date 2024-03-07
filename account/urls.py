from django.urls import path, include
from rest_framework.routers import SimpleRouter,DefaultRouter

from . import views

app_name='account'

router = DefaultRouter()
router.register('users',views.UserViewsets,basename="users")

urlpatterns = [
    path('',include(router.urls)),
    path("dj-rest-auth/login/", views.CustomLoginView.as_view(),name='custom_login'),
    path("dj-rest-auth/", include("dj_rest_auth.urls")), 
]