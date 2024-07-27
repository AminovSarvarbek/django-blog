from django.urls import path
from .views import (
	homeView, 
	blogView, 
	blogDetail,
	videoView,
)


app_name = 'blog'
urlpatterns = [
	path('', homeView, name='home'),
	path('blogs/', blogView, name='blog'),
	path('blog/<int:id>/', blogDetail, name='detail'),

	path('videos/', videoView, name='video'),
]