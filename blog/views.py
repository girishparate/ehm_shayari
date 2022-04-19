from django.shortcuts import render
from .models import Post
import datetime
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import Http404


# Create your views here.
def index(request):
	week_ago = datetime.date.today() - datetime.timedelta(days = 7)
	trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')

	posts = Post.objects.filter(publish=True).order_by("-id")
	paginator = Paginator(posts, 6)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	
	context = {
        'posts': posts,
		'trends': trends[:5],
		'pop_post': Post.objects.order_by('-read')[:9],
    }
	return render(request, 'blog/index.html', context)


def hindi(request):
	hindi = Post.objects.filter(category='Hindi')

	context = {
        'hindi': hindi,
		'pop_post': Post.objects.order_by('-read')[:5],
    }
	return render(request, 'blog/hindi.html', context)


def english(request):
	english = Post.objects.filter(category='English')

	context = {
        'english': english,
		'pop_post': Post.objects.order_by('-read')[:5],
    }
	return render(request, 'blog/english.html', context)


def marathi(request):
	marathi = Post.objects.filter(category='Marathi')

	context = {
        'marathi': marathi,
		'pop_post': Post.objects.order_by('-read')[:5],
    }
	return render(request, 'blog/marathi.html', context)


def post(request, id, slug):
	try:
		post = Post.objects.get(pk=id, slug=slug)
	except:
		raise Http404("Post Does Not Exist")

	week_ago = datetime.date.today() - datetime.timedelta(days = 7)
	trends = Post.objects.filter(time_upload__gte = week_ago).order_by('-read')

	post.read += 1
	post.save()

	context = {
		'post': post,
		'trends': trends[:5],
	}
	return render(request, 'blog/blog-single.html', context)
