from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Blogs,Category
from .forms import BlogForm,SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        blogs = Blogs.objects.all()
        return render(request, "index.html",{"blogs":blogs})
    else:
        return HttpResponseRedirect('/login/')
    



def create(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("/index/")
    return render(request, "create.html", {"form":form})

def detail(request,id):
    blog = Blogs.objects.get(pk=id)
    return render(request,"detail.html",{"blog": blog})



def delete_blog(request,id):
        post = Blogs.objects.get(pk=id)
        post.delete()
        return redirect("/index/")
            


def update_blog(request,id):
    blog=Blogs.objects.get(pk=id)
    if request.method=="POST":
        blog.title=request.POST.get("title")
        blog.description=request.POST.get("description")
        blog.author=request.POST.get("author")
        blog.tags=request.POST.get("tags")
        blog.image=request.FILES.get("image")
        blog.save()
        return redirect("/index/")
    return render(request,"update.html",{"blog":blog})


def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def blog_list(request, id):

    categories = Category.objects.get(pk=id)
    blog = Blogs.objects.filter(category=categories)
    return render(request, 'blog_list.html', {'blog': blog, 'categories': categories})

# def dashboard(request):
#     if request.user.is_authenticated:
#         posts = Blogs.objects.all()
#         user = request.user
#         full_name = user.get_full_name()
#         groups = user.groups.all()
#         return render(request, 'dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': groups})
#     else:
#         return HttpResponseRedirect('/login/')



def user_signup(request):
    if request.user.is_authenticated:
        return redirect("/index/")
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                # Check if the 'Author' group exists, if not create it
                group,created = Group.objects.get_or_create(name='Author')
                user.groups.add(group)
                return HttpResponseRedirect('/index/')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password =  form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/index/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/index/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')