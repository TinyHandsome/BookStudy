from django.shortcuts import render, HttpResponse, redirect
from django.template import loader, Context
from datetime import datetime
from blog.models import BlogPost, BlogPostForm

# Create your views here.
'''
def archive(request):
    mypost = BlogPost(title='mocktitle', body='mockbody', timestamp=datetime.now())
    data = {
        'posts': [mypost]
    }
    return render(request, 'archive.html', context={'posts': [mypost]})
'''

'''
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = {'posts': posts}
    return HttpResponse(t.render(c))
'''


'''
def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, 'archive.html', {'posts': posts})
'''

# archive = lambda req: render(req, 'archive.html', {'posts': BlogPost.objects.all()[11:20]})
archive = lambda req: render(req, 'archive.html', {'posts': BlogPost.objects.all()[11:20], 'form': BlogPostForm()})

def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(title=request.POST.get('title'), body=request.POST.get('body'), timestamp=datetime.now(),).save()
    return redirect('/blog/')