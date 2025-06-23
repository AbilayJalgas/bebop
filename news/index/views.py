from django.shortcuts import render
from .models import NewsCategory, News


# Главная страница
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

# Страница выбранной категории
def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=category)

    context = {
        'category': category,
        'news': news
    }
    return render(request, 'category.html', context)

def news_page(request, pk):
    news = News.objects.get(id=pk)

    context = {'news': news}
    return render(request, 'news.html', context)