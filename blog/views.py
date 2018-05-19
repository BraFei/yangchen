from django.shortcuts import render
from .models import Blog
from django.conf import settings
from django.core.paginator import Paginator
import datetime
from django.utils import timezone

def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    currentr_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    return context


def get_7_days_hot_blogs():
	pass


# Create your views here.
def index(req):
	delta = 2
	context = {}
	dates_concentration = []
	today = timezone.now()
	date = today - datetime.timedelta(days=delta)
	blogs = Blog.objects.filter(created_time__lt=today, created_time__gte=date)
	for blog in blogs:
		dates_concentration.append(blog.concentration)   # 浓度值必须要整数
	context['dates_concentration'] = dates_concentration
	context['date'] = date
	context['delta'] = delta
	return render(req, 'home.html', context)


def blog_list(req):
	context = {}
	blogs = Blog.objects.all()
	context = get_blog_list_common_data(req, blogs)
	return render(req, 'blog/blog_list.html', context)
