default_currency = 'USD'    # Global Currency default

verified_currencies = [
    'USD', 'CAD', 'AUD', 'EUR', 'BRL', 'KYD', 'GBP',
    'CZK', 'DKK', 'ARS', 'HKD', 'INR', 'XAF', 'XOF',
]

# Reference for currency information:
# Saved as a tuple, (0: full name, 1: dollar name, 2: cent name)
currency_ref = {
    'USD': ('United States Dollar', 'Dollar', 'Cent'),
    'CAD': ('Canadian Dollar', 'Dollar', 'Cent'),
    'AUD': ('Australian Dollar', 'Dollar', 'Cent'),
    'EUR': ('Euro Dollar', 'Euro', 'Cent'),
    'BRL': ('Brazilian Real', 'Real', 'Centavo'),
    'KYD': ('Cayman Islands Dollar', 'Dollar', 'Cent'),
    'GBP': ('Great Britain Pound', 'Pound', 'Penny'),
    'CZK': ('Czech Koruna', 'Koruna', 'Haléř'),
    'DKK': ('Danish Krone', 'Krone', 'Øre'),
    'ARS': ('Argentine Peso', 'Peso', 'Centavo'),
    'HKD': ('Hong Kong Dollar', 'Dollar', 'Cent'),
    'INR': ('Indian Rupee', 'Rupee', 'Paisa'),
    'XAF': ('Central African Franc', 'Franc', 'Centime'),
    'XOF': ('West African Franc', 'Franc', 'Centime'),
}
