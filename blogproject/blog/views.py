from django.http import HttpResponse
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
import markdown
# Create your views here.

def index(request):
    # return HttpResponse("欢迎访问shin的博客!")
    # return render(request, 'blog/index.html', context={
    #     'title': '我的博客首页',
    #     'welcome': '欢迎访问我的博客首页'
    # })
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/detail.html', context={'post': post})
# 添加markdown修改
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # markdown模块
    # 其中额外添加了extensions参数 这是对markdown语法的拓展,
    # 这里添加了三个
    # extra 本身包含很多拓展
    # condehilite 是语法高亮拓展
    # toc 自动生成目录
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    # return render(request, 'blog/detail.html', context={'post': post})
    return render(request, 'blog/detail.html', context=context)

# 归档页面
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year = year,
                                    created_time__month = month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

# 分类页面
def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})