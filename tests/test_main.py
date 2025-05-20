import pytest
from src.utils import Product, Smartphone, LawnGrass, Category

def test_product_creation_and_str():
    p = Product("Молоко", "Напитки", 100, 10)
    assert p.name == "Молоко"
    assert p.description == "Напитки"
    assert p.price == 100
    assert p.quantity == 10
    assert str(p) == "Молоко, 100 руб. Остаток: 10 шт."

def test_price_getter_setter():
    p = Product("Тест", "Описание", 500, 5)
    assert p.price == 500
    p.price = 700
    assert p.price == 700

def test_price_setter_invalid_value(capsys):
    p = Product("Тест", "Описание", 500, 5)
    p.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    # Значение price не должно поменяться
    assert p.price == 500

def test_add_products_to_category():
    p1 = Product("Хлеб", "Выпечка", 50, 20)
    p2 = Product("Молоко", "Напитки", 80, 10)
    cat = Category("Продукты", "Еда и напитки", [])
    cat.add_product(p1)
    cat.add_product(p2)
    assert len(cat.products) == 2
    assert "Хлеб" in cat.products[0]
    assert "Молоко" in cat.products[1]
    assert str(cat) == "Продукты, количество продуктов: 30 шт."

def test_add_invalid_product_type_raises():
    cat = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        cat.add_product("Не продукт")

def test_product_add_operator():
    p1 = Product("Товар1", "Описание1", 100, 2)
    p2 = Product("Товар2", "Описание2", 200, 3)
    # Сумма стоимостей
    assert p1 + p2 == 100*2 + 200*3

def test_product_add_operator_type_error():
    p = Product("Товар", "Описание", 100, 2)
    s = Smartphone("Телефон", "Смартфон", 500, 1, "высокая", "ModelX", "128GB", "черный")
    with pytest.raises(TypeError):
        _ = p + s

def test_smartphone_attributes():
    phone = Smartphone("iPhone", "Смартфон", 100_000, 5, "высокая", "13 Pro", "512GB", "золотой")
    assert phone.name == "iPhone"
    assert phone.price == 100_000
    assert phone.efficiency == "высокая"
    assert phone.model == "13 Pro"
    assert phone.memory == "512GB"
    assert phone.color == "золотой"

def test_lawngrass_attributes():
    grass = LawnGrass("Трава", "Газон", 500, 10, "Россия", "14 дней", "зеленый")
    assert grass.name == "Трава"
    assert grass.price == 500
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "зеленый"
