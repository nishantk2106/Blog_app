from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import Post



def home(request):
    context={
        'posts':Post.objects.all()  
    }
    return render(request,'blog/home.html',context)

class postListView(ListView):
    model = Post
    template_name='blog/home.html'# <app>/<model>_<viewstype>.html
    context_object_name = 'posts'
    ordering =['-Date_posted']
    paginate_by = 2

class UserpostListView(ListView):
    model = Post
    template_name='blog/user_post.html'# <app>/<model>_<viewstype>.html
    context_object_name = 'posts'
    ordering =['-Date_posted']
    paginate_by = 5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(Author=user).order_by('-Date_posted')

class PostDetailView(DetailView):
    model = Post
                            # <app>/<model>_<viewstype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Title', 'content']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['Title', 'content']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html',{'title':'About'})