from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # приватный атрибут для хранения цены
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @abstractmethod
    def __str__(self):
        pass


class InfoMixin:
    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"{cls_name} создан с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class Product(InfoMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        if isinstance(other, Product) and type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Нельзя складывать товары разных типов")

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    @classmethod
    def new_product(cls, data: dict):
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

class Smartphone(Product):
    def __init__(self, name, description, _price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, _price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, _price, quantity, country, germination_period, color):
        super().__init__(name, description, _price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []

        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        return [f"{product.name}, {product._price} руб. Остаток: {product.quantity} шт." for product in self.__products]


product1 = Product("Laptop", "High-end laptop", 1500, 5)
product2 = Product("Smartphone", "Latest model smartphone", 800, 10)


category = Category("Electronics", "All kinds of electronic devices", [product1, product2])


print(f"Total categories: {Category.category_count}")
print(f"Total products: {Category.product_count}")

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)