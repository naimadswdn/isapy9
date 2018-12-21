class Chair(object):
    def __init__(self, model='Wing', legs_amount=4,  material_type='plastic', color='dark', net_price=20, margin=10):
        self.legs_amount = legs_amount
        self.armrest_amount = 0
        self.back = True
        self.size = (80, 40, 40)
        self.company = 'Bodzio'

        self.model = model
        self.color = color
        self.material_type = material_type
        self.net_price = net_price
        self.margin = margin

    def sales_price(self):
        return self.net_price * (1 + self.margin/100)

    def price_gross(self):
        return self.sales_price() * 1.23

    def price_gross_eur(self):
        return self.price_gross() * 4.30

    def __str__(self):
        return f"My name is {self.model} and my price is {round(self.price_gross(),2)}"

    def __add__(self, other):
        leg_sum = self.legs_amount + other.legs_amount
        return leg_sum

    def __eq__(self, other):
        net_price = self.net_price == other.net_price
        return net_price

    def __lt__(self, other):
        if self.legs_amount < other.legs_amount:
            print(f'{other.model} is better.')
        else:
            print(f'{self.model} is better.')



Wing = Chair()
Nord = Chair('Nord',5, 'wood', 'wooden', 30)

print(Wing.material_type)
print(Nord.material_type)
print(Nord.price_gross())


print(Nord.price_gross_EUR())
print(Wing.price_gross_EUR())


legs_sum = Chair.__add__(Wing, Nord)
print(legs_sum)
print(Nord + Wing)

print(Chair.__eq__(Wing, Nord))

Nord < Wing

print(Nord)
Wing.__lt__(Nord)
