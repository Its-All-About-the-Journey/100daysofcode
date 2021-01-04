# Constants
MIN_HEIGHT = 120
AGE_TIER3  = 18
AGE_TIER2  = 12
TIER3_FEE  = 12
TIER2_FEE  = 7
TIER1_FEE  = 5

TOTAL_MSG = 'Your total is ${:.2f}'

print('='*80)

print('Welcome to the self-serve ticketing system.')
height = float( input('Enter your height in cm: ') )

# Decide if customer can enter ride and if so, how much it will cost.
if height >= MIN_HEIGHT:
    age = int( input('Enter your age: ') )

    if age >= AGE_TIER3:
        print(TOTAL_MSG.format(TIER3_FEE))
    elif age > AGE_TIER2:
        print(TOTAL_MSG.format(TIER2_FEE))
    else:
        print(TOTAL_MSG.format(TIER1_FEE))
else:
    print(f'Sorry, you are too short for this ride.  Next time wear shoes that add {MIN_HEIGHT - height} cm.')

print('='*80)


# Test cases:
#       Height: 
#           MIN_HEIGHT > height
#           MIN_HEIGHT <= height
# 
#       Age:
#           AGE_TIER3 <= age
#           AGE_TIER2 < age < AGE_TIER3
#           AGE_TIER2 > age 