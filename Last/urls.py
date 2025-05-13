from django.contrib import admin
from django.urls import path, include
from last2.views.auth import CustomUserAPIView          
from last2.views.comment import CommentAPIView, CommentDetailAPIView
from last2.views.news import NewsAPIView, NewsDetailAPIView
from last2.views.qidiruv import NewsSearchAPIView 
from last2.views.statistika import LatestNewsAPIView,  MostViewedNewsAPIView, LastFiveNewsAPIView
from last2.views.save_news import SaveAPIView,SaveDetailAPIView     

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/', CustomUserAPIView.as_view()),
    
    path('news/', NewsAPIView.as_view()),
    path('news/<int:pk>/', NewsDetailAPIView.as_view()),
    
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view()),
    
    
    path('news/latest/', LatestNewsAPIView.as_view()),
    path('news/most-viewed/', MostViewedNewsAPIView.as_view()),
    path('news/last-5/', LastFiveNewsAPIView.as_view()),
    
    path('news/save/', SaveAPIView.as_view()),
    path('news/save/<int:pk>/', SaveDetailAPIView.as_view()),
    
    path('api/search/', NewsSearchAPIView.as_view()),
    
    

]