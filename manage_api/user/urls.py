from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import UserView

app_urls = [path("user/", UserView.as_view(), name="user")]
app_name = "user"
urlpatterns = app_urls + router.urls
