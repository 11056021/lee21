from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
<<<<<<< HEAD
from django.shortcuts import redirect
# Create your views here.
=======
# Create your views here.

>>>>>>> 045b9eed20eaf332a7662fb70bf72b629cbd3cb7
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
<<<<<<< HEAD
    try:
        post = Post.objects.get(slug=slug) #select * from post where slug%=slug
        if post != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
    #如果是空的或找不到就會跳回主頁
=======
    post = Post.objects.get(slug=slug) #select * from post where slug%=slug
    return render(request, 'post.html', locals())

>>>>>>> 045b9eed20eaf332a7662fb70bf72b629cbd3cb7
'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter,post in enumerate(posts):
        post_lists.append(f"No.{counter}-{post}<br>")
    return HttpResponse(post_lists)
'''