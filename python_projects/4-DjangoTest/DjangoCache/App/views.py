import random
from io import BytesIO
from time import sleep

from PIL import ImageFont
from PIL.ImageDraw import Draw, ImageDraw, Image
from django.core.cache import cache, caches
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from App.models import Student
from App.utils import get_color, generate_code
from DjangoCache import settings


def index(request):
    return HttpResponse('Index')


# @cache_page(30)
def news(request):
    temp_cache = caches['redis_backend']
    result = temp_cache.get("news")
    # 如果缓存中能找到news对应的值，直接返回该值
    if result:
        return HttpResponse(result)

    news_list = []
    for i in range(10):
        news_list.append("最近贸易战又开始了 %d" % i)

    sleep(5)

    data = {
        'news_list': news_list
    }

    # 如果缓存中没有找到news的值，则返回response，并将内容写入到缓存中
    response = render(request, 'news.html', context=data)
    cache.set('news', response.content, timeout=60)

    return response


@cache_page(60, cache='redis_backend')
def jokes(request):
    sleep(5)
    return HttpResponse('狗贼')


def home(request):
    return HttpResponse("Home")


def get_phone(request):
    if random.randrange(100) > 95:
        return HttpResponse("恭喜您，抢到小米8了！")
    return HttpResponse("正在排队。。。")


def get_ticket(request):
    if random.randrange(100) > 10:
        return HttpResponse("还剩余99张满100-99")
    return None


def search(request):
    return HttpResponse("这是你搜索到的种子资源")


def calc(request):
    a = 250
    b = 250
    result = (a + b) / 0
    return HttpResponse(result)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        receive_code = request.POST.get("verify_code")
        store_code = request.session.get("verify_code")

        if receive_code.lower() != store_code.lower():
            return redirect(reverse('app:login'))
        return HttpResponse("登录成功！")
    return None


def add_students(request):
    for i in range(100):
        student = Student()
        student.s_name = "小明%d" % i
        student.s_age = i
        student.save()

    return HttpResponse("学生创建成功")


def get_students(request):
    page = int(request.GET.get("page", 1))
    per_page = int(request.GET.get("per_page", 10))
    students = Student.objects.all()[per_page * (page - 1): page * per_page]
    data = {
        "students": students
    }
    return render(request, 'students.html', context=data)


def get_students_with_page(request):
    page = int(request.GET.get("page", 1))
    per_page = int(request.GET.get("per_page", 10))

    students = Student.objects.all()
    paginator = Paginator(students, per_page)

    page_obj = paginator.page(page)
    data = {
        "page_object": page_obj,
        "page_range": paginator.page_range,
    }
    return render(request, 'students_with_page.html', context=data)


def get_code(request):
    # 初始化画布，初始化画笔
    mode = 'RGB'
    size = (200, 100)
    red = get_color()
    green = get_color()
    blue = get_color()

    color_bg = (red, green, blue)
    image = Image.new(mode=mode, size=size, color=color_bg)
    imagedraw = ImageDraw(image, mode=mode)
    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(len(verify_code)):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(10000):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()
    image.save(fp, "png")
    return HttpResponse(fp.getvalue(), content_type="image/png")


