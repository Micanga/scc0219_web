from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('blogs/', views.BlogListView.as_view(), name='blogs'),
	path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
	path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
	path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='blogger-detail'),
	path('<int:pk>/comment/', views.BlogCommentView.as_view(), name='blog_comment'),
]