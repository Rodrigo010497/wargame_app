from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.phases, name="phases"),
    path("<str:phase>/", views.change_view_phase, name="change_view_phase"),
]