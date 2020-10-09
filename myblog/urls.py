from django.urls import path
# from . import views
from .views import HomeView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blogs/<int:pk>', BlogDetailView.as_view(), name='blog-details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('blogs/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('blogs/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('blogs/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]	