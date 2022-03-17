from django.urls import path
from api import views

urlpatterns = [
    # Auth
    path('signup/', views.signup),
    path('login/', views.login),

    # Favorite
    path('favorites/<pk>', views.FavoritesList.as_view()),
]