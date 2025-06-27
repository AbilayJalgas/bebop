from django.shortcuts import render, redirect
from .models import NewsCategory, News
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


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

# Пойск новостей
def search(request):
    if request.method == 'POST':
        get_news = request.POST.get('search_news')
        searched_news = News.objects.filter(news_title__iregex=get_news)

        if searched_news:
            context = {
                'news': searched_news,
                'request': get_news
            }
            return render(request, 'result.html', context)
        else:
            context = {
                'news': '',
                'request': get_news
            }
            return render(request, 'result.html', context)


# Регистрация
class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)

            user.save()

            login(request, user)
            return redirect('/')

# Выход из аккаунта
def logout_view(request):
    logout(request)
    return redirect('/')