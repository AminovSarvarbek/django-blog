from django.shortcuts import render ,HttpResponse
from .models import Blog
from .utils import blog_list_by_year_month


def homeView(request):
	return render(request, 'home.html', {})

def blogView(request):
	blogs = Blog.objects.all()
	grouped_blogs = blog_list_by_year_month(blogs)
	return render(request, 'blog/list.html', {'grouped_blogs': grouped_blogs})


def blogDetail(request, id):
	try:
		blog = Blog.objects.get(id=id)
		return render(request, 'blog/detail.html', {'blog':blog})
	except Exception as e:
		print(e)
		return HttpResponse('404')



# videos
def videoView(request):
	blogs = Blog.objects.filter(is_video=True)
	grouped_blogs = blog_list_by_year_month(blogs)
	return render(request, 'blog/list.html', {'grouped_blogs': grouped_blogs, 'video':True})
