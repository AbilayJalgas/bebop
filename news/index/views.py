from django.shortcuts import render, redirect
from .models import NewsCategory, News, Favourites
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

# Добавление товара в избранное
def add_to_favourites(request, pk):
    if request.method == "POST":
        news = News.objects.get(id=pk)


        Favourites.objects.create(user_id=request.user.id,
                                  user_favourites=news).save()

        return redirect(f'/news/{pk}')

# Удаление товара из избранных
def del_from_favourites(request, pk):
    news_to_del = News.objects.get(id=pk)
    Favourites.objects.filter(user_favourites=news_to_del).delete()

    return redirect('/favourites')

# Отображение избранных
def show_favourites(request):
    user_favourites = Favourites.objects.filter(user_id=request.user.id)

    context = {
        'favourites': user_favourites,
    }

    return render(request, 'favourites.html', context)