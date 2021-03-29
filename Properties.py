class Property:
    """Superclass that provides basic information for both appartment and house classes"""
    def __init__(self, footage='', bedrooms='', bathrooms='', **kwargs):
        """Instantiates property object with footage, number of bedrooms, bathrooms """
        super().__init__(**kwargs)
        self.footage = footage
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def display(self):
        """
        Method that displays information about chosen property`s facilities
        """
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


class Appartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        """
        Method that displays information about chosen appartment`s facilities
        """
        super().display()
        print('=======APPARTMENT DETAILS=========')
        print(f'number of balconies: {self.balcony}')
        print(f'number of laundries: {self.laundry}')


    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input('What loundry facilities does property have?', Appartment.valid_laundries)
        balcony = get_valid_input('Does the property have a balcony?', Appartment.valid_balconies)
        parent_init.update({
            'laundry' : laundry,
            'balcony' : balcony
        })
        return parent_init


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, floors='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.floors = floors
        self.garage = garage
        self.fenced = fenced

    def display(self):
        """
        Method that displays information about chosen house`s facilities
        """
        super().display()
        print('=======HOUSE DETAILS=========')
        print(f'house have {self.floors}')
        print(f'garage is: {self.garage}')
        print(f'is fenced: {self.fenced}')


    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        garage = get_valid_input('What the garage should be?', House.valid_garage)
        fenced = get_valid_input('Should the house be fanced?', House.valid_fenced)
        floors = int(input('How many floors should be?'))
        parent_init.update({
            'floors' : floors,
            'garage' : garage,
            'fenced' : fenced
        })
        return parent_init



def get_valid_input(input_string, valid_words: tuple):
    """returns value it matches one of valid_words """
    input_string += f'{valid_words}'
    response = input(input_string)
    while response.lower() not in ' '.join(valid_words):
        response = input(input_string)
    return response


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print('========Purchase details========')
        print(f'Selling price {self.price}')
        print(f'Estimated taxes {self.taxes}')

    @staticmethod
    def prompt_init():
        return dict(
            price = input('what price should be'),
            taxes = input('what are estimated taxes')
        )

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print('=======Rental details=======')
        print(f'Is furnished {self.furnished}')
        print(f'rent: {self.rent}')
        print(f'Utilities: {self.utilities}')

    @staticmethod
    def prompt_init():
        return dict(
            rent = input('Input rent:'),
            utilities = input('Input utilities:'),
            furnished = get_valid_input(('Should be furnished? (yes, no)', ('yes', 'no')))
        )


r = Rental()
r.display()