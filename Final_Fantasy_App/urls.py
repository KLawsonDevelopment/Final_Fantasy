from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('characters', views.CharacterView)
# router.register('details', views.DetailView)
router.register('pieces', views.PieceView)
router.register('wanted', views.WantedView)

urlpatterns = [
    path('', include(router.urls))
]