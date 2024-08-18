from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        if isinstance(name, str):
            self.name = name
        else:
            print('Название должно быть указано буквами')
        if isinstance(weight, float):
            round(weight, 1)
            self.weight = weight
        else:
            print('Вес должен быть указан до десятых')
        if isinstance(category, str):
            self.category = category
        else:
            print('Категория должна быть указана буквами')

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        try:
            return file.read()
        finally:
            file.close()

    def add(self, *products):
        for product in products:
            if product.name in self.get_products():
                print(f'Продукт "{product.name}" уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product))
                file.write('\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Banana', 33.4, 'Fruits')
p3 = Product('Oat porridge', 22.7, 'Groceries')
s1.add(p1, p2, p3)
print(s1.get_products())
