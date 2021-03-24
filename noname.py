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
        laundry = ''
        while laundry.lower() not in Appartment.valid_laundries:
            laundry = input('What laundry facilities does property have? ({})'
                            .format(", ".join(Appartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Appartment.valid_balconies:
            balcony = input(
                'Does property have a balcony? ({})'
                    .format(', '.join(Appartment.valid_balconies)))
        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })
        return parent_init
    # prompt_init = staticmethod(prompt_init)

ap = Appartment('bal', 'laund', footage = 12, bedrooms=3, bathrooms = 4)
sm = Appartment('bal', 'laund', footage = 12, bedrooms=3, bathrooms = 4)
# print(ap.prompt_init())
# print(Appartment.prompt_init())
print(ap)
print(sm)
