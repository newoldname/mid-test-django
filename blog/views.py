from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


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


class PostDetail(DetailView):
    model = Post
