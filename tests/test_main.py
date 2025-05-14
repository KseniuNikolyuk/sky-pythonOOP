from main import Product, Category  # импортируем классы из main.py

def test_product_creation():
    product = Product("Mouse", "Wireless mouse", 2000, 15)

    assert product.name == "Mouse"
    assert product.description == "Wireless mouse"
    assert product.price == 2000
    assert product.quantity == 15

def test_category_creation():
    product1 = Product("Keyboard", "Mechanical keyboard", 5000, 8)
    product2 = Product("Monitor", "24-inch monitor", 12000, 3)
    category = Category("Accessories", "Computer accessories", [product1, product2])

    assert category.name == "Accessories"
    assert category.description == "Computer accessories"
    assert category.products == [product1, product2]

def test_counters_reset():
    # Сохраняем старые значения счётчиков
    old_categories = Category.total_categories
    old_products = Category.total_products

    product1 = Product("Webcam", "HD webcam", 3000, 4)
    product2 = Product("Headphones", "Noise cancelling", 7000, 2)
    Category("Gadgets", "Office gadgets", [product1, product2])

    assert Category.total_categories == old_categories + 1
    assert Category.total_products == old_products + 2
