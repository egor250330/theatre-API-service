from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from theatre.views import (
    ActorViewSet,
    GenreViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)

app_name = "theatre"

router = routers.DefaultRouter()

router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)
router.register("theatres", TheatreHallViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet, basename="reservation")
router.register("tickets", TicketViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
