from django.shortcuts import render
import json


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {
                "img": "vendor/img/products/Adidas-hoodie.png",
                "title": "Худи черного цвета с монограммами adidas Originals",
                "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
                "price": 6090.00
            },
            {
                "img": "vendor/img/products/Blue-jacket-The-North-Face.png",
                "title": "Синяя куртка The North Face",
                "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
                "price": 23725.00
            },
            {
                "img": "vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "title": "Коричневый спортивный oversized-топ ASOS DESIGN",
                "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
                "price": 3390.00
            },
            {
                "img": "vendor/img/products/Black-Nike-Heritage-backpack.png",
                "title": "Черный рюкзак Nike Heritage",
                "description": "Плотная ткань. Легкий материал.",
                "price": 2340.00
            },
            {
                "img": "vendor/img/products/Black-Dr-Martens-shoes.png",
                "title": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
                "description": "Гладкий кожаный верх. Натуральный материал.",
                "price": 13590.00
            },
            {
                "img": "vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
                "title": "Темно-синие широкие строгие брюки ASOS DESIGN",
                "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
                "price": "2890.00"
            }]
    }

    with open('mainapp/fixtures/products.json', 'r') as json_file:
        json_data = json.load(json_file)

    return render(request, 'mainapp/products.html', context)

# with open('D:\\GitHub\\gbDjango\\geekshop-server\\geekshop\mainapp\\fixtures\\products.json', 'r') as json_file:
#     json_data = json.load(json_file)
#     for i in json_data['products']:
