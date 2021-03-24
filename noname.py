class Property:
    def __init__(self, footage='', bedrooms='', bathrooms='', **kwargs):
        super().__init__(**kwargs)
        self.footage = footage
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def display(self):
        print('========================')
        print(f'square footage = {self.footage}')
        print(f'number of bedrooms = {self.bedrooms}')
        print(f'number of bathrooms = {self.bathrooms}')
        print('========================')

    def prompt_init():
        return dict(footage = input('Enter the square feet: '),
                    bedrooms = input('Enter number of bedrooms: '),
                    bathrooms = input('Enter number of bathrooms: '))
    prompt_init = staticmethod(prompt_init)


class House(Property):
    pass

class Appartment(Property):
    pass

p = Property('235', '4', 5)
# print(p.footage, p.bathrooms, p.bedrooms)
# p.display()
print(p.prompt_init())