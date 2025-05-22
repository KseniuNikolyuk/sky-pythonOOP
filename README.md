# Магазин: Категории и Товары

## Описание

Это простой проект на Python, имитирующий структуру магазина. Содержит два класса:

- `Product` — представляет отдельный товар.
- `Category` — представляет категорию товаров, содержащую список продуктов.

Каждый раз при создании новой категории и добавлении товаров, счётчики категорий и продуктов автоматически увеличиваются.

---

## Структура классов

### Класс `Product`

Хранит информацию о товаре:

- `name` — название товара
- `description` — описание товара
- `price` — цена
- `quantity` — количество на складе

### Класс `Category`

Хранит информацию о категории товаров:

- `name` — название категории
- `description` — описание категории
- `products` — список товаров (объектов `Product`) в категории

Также есть два класса-переменные:

- `category_count` — общее количество созданных категорий
- `product_count` — общее количество товаров, добавленных в категории

---

## Пример использования

```python
product1 = Product("Laptop", "High-end laptop", 1500, 5)
product2 = Product("Smartphone", "Latest model smartphone", 800, 10)

category = Category("Electronics", "All kinds of electronic devices", [product1, product2])

print(Category.category_count)  # 1
print(Category.product_count)   # 2

