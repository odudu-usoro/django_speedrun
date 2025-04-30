from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet
from .views import SignupView

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='posts')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
]