from django.shortcuts import render, redirect
from .models import Blog, Portfolio, Comment, User, Category


def index(request):
    user = User.objects.get(id=1)
    blogs = Blog.objects.all().order_by('-id')[:3]
    portfolios = Portfolio.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('title')

    context = {
        'user': user,
        'blogs': blogs,
        'portfolios': portfolios,
        "categories": categories,
    }

    return render(request, 'index.html', context)

def single(request, slug):
    blog = Blog.objects.get(slug__exact=slug)

    comments = Comment.objects.filter(blog_id=blog.id)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("single")
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        website = request.POST.get("website")

        Comment.objects.create(
            blog_id=blog.id,
            user=request.user,
            name=name,
            email=email,
            comment=comment,
            website=website,
        )

        return redirect('single', blog.slug)

    context = {
        "blog": blog,
        "comments": comments,
        }
    
    return render(request, 'blog-single.html', context)

def grid(request):
    blogs = Blog.objects.all().order_by('-id')

    context = {
        'blogs': blogs,
        }
    
    return render(request, 'blog-grid.html', context)
