NUMBERS_OF_MONTHS = 12
COMPOUND_METHODS = {
                'monthly': 12,
                'quarterly': 4,
                'semi-annually': 2,
                'annually': 1
                }

class Mortgage:
    '''Represents a mortgage
    '''
    
    def __init__(self, principal, down_payment_ratio, mortgage_rate, amortization, compound_method='semi-annually'):
        self.principal = principal
        self.down_payment_ratio = down_payment_ratio
        self.mortgage_rate = mortgage_rate
        self.amortization = amortization
        self.balance = self.loan_amount()
        self.period = 0
        self.compound_periods = COMPOUND_METHODS[compound_method]
        self.total_paid = self.down_payment()
        
    @property
    def principal(self):
        return self.__principal
    
    @principal.setter
    def principal(self, principal):
        if principal <= 0:
            raise ValueError('The principal may not be zero or less')
        else:
            self.__principal = principal
    
    @property
    def down_payment_ratio(self):
        return self.__down_payment_ratio
    
    @down_payment_ratio.setter
    def down_payment_ratio(self, down_payment_ratio):
        if down_payment_ratio <= 0:
            raise ValueError('The down payment ratio may not be zero or less')
        else:
            self.__down_payment_ratio = down_payment_ratio
            
    @property
    def mortgage_rate(self):
        return self.__mortgage_rate
    
    @mortgage_rate.setter
    def mortgage_rate(self, mortgage_rate):
        if mortgage_rate <= 0:
            raise ValueError('The mortgage rate may not be zero or less')
        else:
            self.__mortgage_rate = mortgage_rate
            
    @property
    def amortization(self):
        return self.__amortization
    
    @amortization.setter
    def amortization(self, amortization):
        if amortization <= 0:
            raise ValueError('The amortization period may not be zero years or less')
        else:
            self.__amortization = amortization
    
    def down_payment(self):
        return self.down_payment_ratio * self.principal
    
    def loan_amount(self):
        return self.principal - self.down_payment()
   
    def payment_periods(self):
        return self.amortization * NUMBERS_OF_MONTHS
        
    def effective_interest_rate(self):
        return (1 + (self.mortgage_rate / self.compound_periods)) ** (self.compound_periods / NUMBERS_OF_MONTHS) - 1
    
    def monthly_payment(self):
        monthly_rate = self.effective_interest_rate()
        payment_periods = self.payment_periods()
        loan_amount = self.loan_amount()
        return loan_amount * ((monthly_rate * (1 + monthly_rate) ** payment_periods) / ((1 + monthly_rate) ** payment_periods - 1))
    
    def update_period(self):
        self.period += 1
    
    def update_balance(self):
        self.balance *= 1 + (self.effective_interest_rate())
        self.balance -= self.monthly_payment()
        self.update_period()
        self.update_total_paid()
    
    def update_total_paid(self):
        self.total_paid += self.monthly_payment()
        
class House:
    '''Represents a house
    '''
    def __init__(self, house_price, bedrooms, bathrooms, property_taxes, maintenance_fees):
        self.house_price = house_price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.property_taxes = property_taxes
        self.monthly_taxes = self.property_taxes / NUMBERS_OF_MONTHS
        self.maintenance_fees = maintenance_fees
        self.expenses = 0
        self.month = 0
        
    @property
    def house_price(self):
        return self.__house_price
    
    @house_price.setter
    def house_price(self, house_price):
        if house_price <= 0:
            raise ValueError('The house price may not be zero or less')
        else:
            self.__house_price = house_price
    
    @property
    def bedrooms(self):
        return self.__bedrooms
    
    @bedrooms.setter
    def bedrooms(self, bedrooms):
        if bedrooms < 0:
            raise ValueError('The number of bedrooms may not be negative')
        else:
            self.__bedrooms= bedrooms
    
    @property
    def bathrooms(self):
        return self.__bathrooms
    
    @bathrooms.setter
    def bathrooms(self, bathrooms):
        if bathrooms < 0:
            raise ValueError('The number of bedrooms may not be negative')
        else:
            self.__bathrooms = bathrooms
    
    @property
    def property_taxes(self):
        return self.__property_taxes
    
    @property_taxes.setter
    def property_taxes(self, property_taxes):
        if property_taxes < 0:
            raise ValueError('Property taxes may not be negative')
        else:
            self.__property_taxes = property_taxes
    
    @property
    def maintenance_fees(self):
        return self.__maintenance_fees
    
    @maintenance_fees.setter
    def maintenance_fees(self, maintenance_fees):
        if maintenance_fees < 0:
            raise ValueError('Maintenance fees may not be negative')
        else:
            self.__maintenance_fees = maintenance_fees
    
    def update_house_price(self, growth_rate):
        self.house_price *= (1 + growth_rate)
        self.update_expenses()
        
    def update_expenses(self):
        monthly_property_taxes = self.property_taxes / NUMBERS_OF_MONTHS
        self.expenses += monthly_property_taxes + self.maintenance_fees
        self.update_month()
        
    def update_month(self):
        self.month += 1