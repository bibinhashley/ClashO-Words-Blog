from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)

        if userform.is_valid():
            userform.save()
            username = userform.cleaned_data['username']
            messages.success(request, "Registered successfully!")
            return redirect('login')

    else:
        userform = UserForm()
    return render(request, 'user/register.html', {'userform': userform})


def logout_request(request):
    logout(request)
    messages.success(request, "You are successfully logged out")
    return redirect("home")


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = 'user/login.html'
    success_message = "You are successfully logged in"


@login_required
def profile(request, username):

    user = User.objects.get(username=username)
    return render(request, 'user/profile.html', )


@login_required
def addsocial(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        profileform = ProfileForm(request.POST, instance=request.user.profile)
        if profileform.is_valid():
            profileform.save()
            return redirect('profile', user)
    else:

        profileform = ProfileForm(instance=request.user.profile)
    return render(request, 'user/addsocial.html', {'profileform': profileform})


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'user/post.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'drafts'
    ordering = ['-date_created']

    queryset = Post.objects.filter(
        date_published__isnull=True)


class PublishedPosts(ListView):
    redirect_field_name = 'blog/post_list.html'
    context_object_name = 'published_posts'
    ordering = ['-date_created']
    model = Post
    queryset = Post.objects.filter(
        date_published__isnull=False)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    model = Post


@login_required()
def save_draft(request):
    model = Post
    fields = ['title', 'content']
    template_name = 'user/post.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user

        return super().form_valid(form)


@login_required()
def save_draft(request):
    pass


class PostDetail(DetailView):
    model = Post
    template_name = 'user/post_detail.html'
    context_object_name = 'post_detail'
