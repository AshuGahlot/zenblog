from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm
from django.template.defaultfilters import slugify

# Create your views here.


# Dashboard function 
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()
    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts
    }
    return render(request, 'dashboard/dashboard.html',context)


# Leftside bar categories function 

def categories(request):
    return render(request, 'dashboard/categories.html')


# Add category 
def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoryForm()
    
    context = {
        'form':form
    }
    return render(request, 'dashboard/add_categories.html',context)



# Edit Categories 
def edit_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }
    return render(request, 'dashboard/edit_categories.html',context)



# Delete Categories 
def delete_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')



# Show all posts Function 
def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'dashboard/posts.html', context)



# Post Functions

# Add Post Function
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            return redirect('posts')
        else:
            print('error')
    form = BlogPostForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)



# Edit post function 
def edit_post(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'dashboard/edit_post.html',context)



# Delete Post
def delete_post(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('posts')