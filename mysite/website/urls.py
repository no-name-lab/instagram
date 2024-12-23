from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'follows', FollowViewSet, basename='follow-list')
router.register(r'posts', PostViewSet, basename='post-list')
router.register(r'post_likes', PostLikeViewSet, basename='post_likes-list')
router.register(r'comments', CommentViewSet, basename='comment-list')
router.register(r'comment_likes', CommentLikeViewSet, basename='comment_likes-list')
router.register(r'stories', StoryViewSet, basename='stories-list')
router.register(r'saves', SaveViewSet, basename='save-list')
router.register(r'save_items', SaveItemViewSet, basename='save_item-list')
router.register(r'chat', ChatViewSet, basename='chat-list')
router.register(r'message', MessageViewSet, basename='message-list')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]






