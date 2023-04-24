from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Post, Category, Tag


# Create your views here.

# region FVB
# def index(request):
#     # posts = Post.objects.all()
#     posts = Post.objects.all().order_by("-pk")
#
#     return render(
#         request,
#         "blog/index.html",
#         {
#             "posts": posts,
#         },
#     )


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         "blog/single_post_page.html",
#         {
#             "post": post,
#         },
#     )
# endregion


class PostList(ListView):
    model = Post
    ordering = "-pk"
    # 기본적으로 해당 클래스는 "{모델명}_list.html"을 사용하고.
    # 랜더링할 변수 이름도 단순히 posts가 아닌 "{모델명}_list"이다.
    # 만약에 템플릿 을 강제로 지정하고 싶으면
    # template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context["category"] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context["category"] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count()
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "head_image", "file_upload", "category", "tags"]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect("/blog/")

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context["category"] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count()
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "head_image", "file_upload", "category", "tags"]

    template_name = 'blog/post_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        context["category"] = Category.objects.all()
        context["no_category_post_count"] = Post.objects.filter(category=None).count()
        return context

def categories_page(request, slug):
    if slug == "no-category":
        category = "무분류"
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)

    return render(
        request,
        "blog/post_list.html",
        {
            "post_list": posts,
            "category": Category.objects.all(),
            "category_name": category,
            "no_category_post_count": Post.objects.filter(category=None).count(),
        },
    )


def tags_page(request, slug):
    if slug == "no-tag":
        tag = "무분류"
        posts = Post.objects.filter(tags=None)
    else:
        tag = Tag.objects.get(slug=slug)
        # posts = Post.objects.filter(tags=tag) # 이거도 잘 되더라
        posts = tag.post_set.all()

    return render(
        request,
        "blog/post_list.html",
        {
            "post_list": posts,
            "category": Category.objects.all(),
            "tag_name": tag,
            "no_category_post_count": Post.objects.filter(category=None).count(),
        },
    )
