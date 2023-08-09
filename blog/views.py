import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm

def posts(request):

    posts = Post.objects.all()
    data = {
        'posts':posts
    }
    return render(request,"posts.html",data)


def post(request,blog_id):
    post = Post.objects.get(id=blog_id)
    context = {
        'post':post
    }
    return render(request,"post-details.html",context)

def about(request):
    return render(request,"about-us.html")

def add_post(request):
    template_name = 'add_post.html'
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        print(form.errors.as_data())
        print(form)
        if form.is_valid():
            form.save()
        # new_post = Post.objects.create(
        # title = request.POST['title'],
        # image =  request.FILES.get('image'),
        # description =  request.POST.get('description')
        # )
        messages.info(request,'Post successfully created.')
        return redirect('blog:posts')
    form = PostForm()
    return render(request, template_name,{'form':form})

def delete_post(request, id):
    template_name = 'delete_post.html'
    obj = Post.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        messages.info(request,'Post with title "{}" was successfully deleted.'.format(obj.title))
        return redirect('blog:posts')
    return render(request, template_name,{'obj':obj})

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        if title and description:
            post.title = title
            post.description = description
            if image:
                post.image = image
            post.save()

            messages.success(request, f'Post with title "{title}" was successfully updated.')
            return redirect('blog:posts')

    context = {
        'editobj': post,
    }    
    return render(request, 'edit_post.html', context)




def comments(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    Comment.objects.create(
        post=post,
        comment = request.POST.get('comment')
    )
    return redirect('blog:post', post_id)