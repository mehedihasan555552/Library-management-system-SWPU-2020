from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def index(request):
    books = Book.objects.all()
    context ={'books':books}
    return render(request,'base/index.html',context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + username)
            return redirect('index')
    context={'form':form}
    return render(request,'base/signup.html',context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['book_name','author_name','pic','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Book


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['book_name','author_name','pic','status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def Insert(request):
    form = Bookborrow()
    if request.method == 'POST':
        form = Bookborrow(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')
    context={'form':form}
    return render(request,'base/insert.html',context)



def View(request):
    user = Borrow.objects.all()
    content = {'user':user}
    return render(request,'base/view.html',content)



def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')

        else:
            messages.info(request,'username or password incorrect.')
    context={}
    return render(request, 'base/login.html',context)



def userlogout(request):
    logout(request)
    return redirect('index')
