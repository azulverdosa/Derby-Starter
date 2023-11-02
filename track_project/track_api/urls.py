from django.urls import include, path

from rest_framework import routers

from track_api.views import ScheduleViewSet, TeamViewSet, SkaterViewSet

router = routers.DefaultRouter()
router.register(r'schedule', ScheduleViewSet)
router.register(r'team', TeamViewSet)
router.register(r'skater', SkaterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]