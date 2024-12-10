from django.shortcuts import render


def one(request):
    text = 'Главная страница'
    context = {
        'text1': text
    }
    return render(request, "platform.html", context)


def two(request):
    text = 'Игры'
    context = {
        'text2': text,
        'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    }
    return render(request, "games.html", context)


def three(request):
    text = 'Извините, ваша корзина пуста'
    context = {
        'text3': text
    }
    return render(request, "cart.html", context)