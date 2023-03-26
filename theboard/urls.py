from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, AddCommentView, DashboardView


urlpatterns = [        
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),    
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/disapprove/', views.comment_disapprove, name='comment_disapprove'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('user/<int:pk>/subscribe/', views.news_subscribe, name='news_subscribe'),
]
