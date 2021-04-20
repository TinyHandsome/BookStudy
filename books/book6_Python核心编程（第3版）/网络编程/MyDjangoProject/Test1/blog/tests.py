from django.test import TestCase
from django.test.client import Client
from datetime import datetime
from blog.models import BlogPost

class BlogPostTest(TestCase):
    def test_obj_create(self):
        """通过测试确保对象成功创建，并验证标题的内容"""
        BlogPost.objects.create(title='raw title', body='raw body', timestamp=datetime.now())
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('raw title', BlogPost.objects.get(id=1).title)

    def test_home(self):
        """检测用户界面"""
        response = self.client.get('/blog/')
        self.failUnlessEqual(response.status_code, 200)

    def test_slash(self):
        """检测用户界面"""
        response = self.client.get('/')
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        """测试某人在没有任何数据就错误地生成GET 请求这样的情形，代码应该忽略这个请求，并重定向"""
        response = self.client.get('/blog/create/')
        self.assertIn(response.status_code, (301, 302))

    def test_post_create(self):
        """模拟真实用户请求通过POST发送真实数据"""
        response = self.client.post('/blog/create/', {
            'title': 'post title',
            'body': 'post body',
        })
        self.assertIn(response.status_code, (301, 302))
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('post title', BlogPost.objects.get(id=1).title)
