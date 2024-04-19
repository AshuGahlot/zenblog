from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from .models import Blogs,Category,Comment
from django.db.models import Q



# Create your views here.

def post_by_category(request,category_id):
    posts = Blogs.objects.filter(status='published',category= category_id)
# When you want show any custom message then use try except block 
    # try:
    #     category = Category.objects.get(pk = category_id)
    # except:
    #     return redirect('')

# If you want to show 404 error then use get_object_or_404
    category = get_object_or_404(Category, pk=category_id)

    context ={
        'posts':posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)



# Blogs 

def blogs(request,slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    
    # comment form 
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    #show comment
    comments = Comment.objects.filter(blog=single_post)
    comment_count = comments.count()
    context = {
        'single_post': single_post,
        'comments' : comments,
        'comment_count': comment_count
    }
    return render(request, 'blogs.html', context)




# Search

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword), status='published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request, 'search.html',context)


