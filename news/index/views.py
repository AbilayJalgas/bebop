from django.shortcuts import render
from .models import NewsCategory, News

# Достаем данные
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()

    # Передаем данные на фронт
    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'home.html', context)