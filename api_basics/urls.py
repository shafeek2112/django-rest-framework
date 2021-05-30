from django.urls import path, include
# from .views import article, article_detail
# from .views import ArticleAPIView, ArticleDetailAPIView
# from .views import ArticleGenericAPIView,ArticleDetailGenericAPIView
# from .views import ArticleViewSets
# from .views import ArticleGenericViewSets
from .views import ArticleModelViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'article', ArticleViewSets, basename='article')
router.register(r'article', ArticleModelViewSets, basename='article')

urlpatterns = [
    # Function based urls
    # path('article/',article, name="article"),
    # path('article-detail/<int:pk>/',article_detail, name="article-detail"),
   
    # Class based urls
    # path('article/',ArticleAPIView.as_view(), name="article"),
    # path('article-detail/<int:id>/',ArticleDetailAPIView.as_view(), name="article-detail"),

    # Generic Class based urls
    # path('article/',ArticleGenericAPIView.as_view(), name="article"),
    # path('article/<int:id>/',ArticleDetailGenericAPIView.as_view(), name="article"),
    
    # Viewsets (no need to mention the 'article', becaues its mentioned in router above.)
    path('',include(router.urls)),
]