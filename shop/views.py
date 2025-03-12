from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def catalog(request):
    return render(request, 'catalog.html')

def about(request):
    return render(request, 'about.html')

def task1(request):
    sorted_books = []

    if request.method == "POST":
        books_input = request.POST.get("books", "").strip()  # Получаем строку от пользователя

        if not books_input:
            messages.error(request, "Введите данные о книгах.")
            return render(request, 'task1.html', {'sorted_books': sorted_books})

        try:
            books_list = books_input.split(",")  # Разделяем по запятой
            books = []

            for item in books_list:
                try:
                    # Разделяем по последнему дефису
                    name, pages = item.rsplit("-", 1)
                    name = name.strip()
                    pages = int(pages.strip())

                    if pages < 200:  # Оставляем только книги с менее чем 200 страницами
                        books.append((name, pages))
                except ValueError as e:
                    # Обработка ошибок при разделении или преобразовании страниц в число
                    messages.error(request, f"Ошибка в формате данных: {item}. Убедитесь, что данные введены в формате 'Название книги-Количество страниц'.")
                    continue

            if not books:
                messages.warning(request, "Нет книг с количеством страниц менее 200.")
            else:
                # Сортируем по количеству страниц (по убыванию), а затем по названию (по убыванию)
                books.sort(key=lambda x: (-x[1], x[0]), reverse=False)

                # Получаем только названия книг
                sorted_books = [book[0] for book in books]

        except Exception as e:
            # Обработка общих ошибок
            messages.error(request, f"Произошла ошибка: {str(e)}")

    return render(request, 'task1.html', {'sorted_books': sorted_books})


def task2(request):
    result = None
    x = a = b = None  # Инициализируем переменные

    if request.method == "POST":
        x = int(request.POST.get("x"))
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))

        result = a <= x <= b  # Проверяем, входит ли X в [a, b]

    return render(request, 'task2.html', {'result': result, 'x': x, 'a': a, 'b': b})


def requirements(request):
    return render(request, 'creators.html')
