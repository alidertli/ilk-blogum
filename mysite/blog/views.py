from django.shortcuts import render
from .models import Ali
from django.utils import timezone

def post_list(request):
    posts = Ali.objects.filter(yayinlama_tarihi__lte=timezone.now()).order_by('yayinlama_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})
