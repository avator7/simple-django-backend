from django.shortcuts import render
from blog.models import Post

# Create your views here.
def bloghome(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)
    

def blogpost(request, slug):
    return render(request,'blog/blogpost.html')