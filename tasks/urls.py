from django.urls import path
from tasks.views import show_task, show_new_features

urlpatterns = [
    path("show-task/", show_task)
    path("show_feature/<int:id>/", show_new_features)
]
