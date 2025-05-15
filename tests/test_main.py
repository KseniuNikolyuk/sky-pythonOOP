from src.utils import Category, Product


def test_add_product():
    product = Product("Test Phone", "Test Description", 10000.0, 3)
    category = Category("Тестовая категория", "Описание", [])
    category.add_product(product)

    assert len(category.products) == 1
    assert "Test Phone" in category.products[0]


def test_product_str():
    p = Product("Молоко", "Напитки", 80, 15)
    assert str(p) == "Молоко, 80 руб. Остаток: 15 шт."


def test_product_add():
    p1 = Product("Молоко", "Напитки", 80, 10)
    p2 = Product("Хлеб", "Выпечка", 40, 5)
    assert p1 + p2 == 80 * 10 + 40 * 5


def test_price_getter_and_setter():
    product = Product("Test Product", "Description", 5000, 2)
    assert product.price == 5000

    product.price = 7000
    assert product.price == 7000


def test_price_setter_with_invalid_value(capsys):
    product = Product("Test Product", "Description", 5000, 2)
    product.price = -300

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 5000


def test_category_str():
    p1 = Product("Молоко", "Напитки", 80, 10)
    p2 = Product("Хлеб", "Выпечка", 40, 5)
    cat = Category("Продукты", "Еда и напитки", [p1, p2])
    assert str(cat) == "Продукты, количество продуктов: 15 шт."
