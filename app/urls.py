from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AvaliacaoViewSet

router = DefaultRouter()
router.register(r"avaliacoes", AvaliacaoViewSet, basename="avaliacao")

urlpatterns = router.urls
