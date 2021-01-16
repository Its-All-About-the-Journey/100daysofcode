# 100 Days of Code : Day 15 Project
# Coffee Machine Data
# Adam Pawlowski (@hypermanganate)

resources = {
 'Water':
  {
    'unit': 'ml',
    'value' : 300
  },
  'Milk':
  {
    'unit' : 'ml',
    'value' : 200
  },
  'Coffee':
  {
    'unit': 'g',
    'value': 100
  },
  'Money':
  { 
    'unit': '',
    'value': 0
  }
}

recipe = {
  'espresso': {
    'Milk': 0,
    'Water': 50,
    'Coffee': 18,
  },
  'latte': {
    'Milk': 150,
    'Water': 200,
    'Coffee': 24,
  },
  'cappuccino': {
    'Milk': 100,
    'Water': 250,
    'Coffee': 24,
  }
}

prices = {
  'espresso': 1.50,
  'latte': 2.50,
  'cappuccino': 3.00
}

coin_values = {
  'pennies': 0.01,
  'nickels': 0.05,
  'dimes': 0.10,
  'quarters': 0.25
}

machine_actions = ['espresso', 'latte', 'cappuccino', 'off', 'report']
