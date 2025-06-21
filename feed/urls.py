from django.urls import path
from . import views

urlpatterns = [
    path("feeds/", views.feed_list, name="feed_list"),
    path("feeds/<int:id>", views.s_feed, name="s_feed"),
    path("feeds/create", views.create_feed, name="create_feed"),
    path("feeds/edit/<int:id>", views.edit_feed, name="edit_feed"),
    path("feeds/delete/<int:id>", views.delete_feed, name="delete_feed"),
    path("welcome/", views.welcome_feed, name="welcome_feed"),
    path('unauthorized/', views.unauthorized, name='unauthorized')
]
