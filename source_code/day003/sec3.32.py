# Constants
MIN_HEIGHT = 120
AGE_TIER3  = 18
AGE_TIER2  = 12
TIER3_FEE  = 12
TIER2_FEE  = 7
TIER1_FEE  = 5
PHOTO_FEE  = 3

TICKET_COST_MSG = 'Your ticket is ${:.2f}'
TOTAL_COST_MSG  = 'Your total cost is ${:.2f}'
print('='*80)

print('Welcome to the self-serve ticketing system.')
height = float( input('Enter your height in cm: ') )

# Decide if customer can enter ride and if so, how much it will cost.
if height >= MIN_HEIGHT:
    age = int( input('Enter your age: ') )

    if age >= AGE_TIER3:
        fee = TIER3_FEE
        print(TICKET_COST_MSG.format(TIER3_FEE))
    elif age > AGE_TIER2:
        fee = TIER2_FEE
        print(TICKET_COST_MSG.format(TIER2_FEE))
    else:
        fee = TIER1_FEE
        print(TICKET_COST_MSG.format(TIER1_FEE))
    
    include_photo = input('Do you ant a photo taken? Y or N. ')

    if include_photo == 'Y':
        fee += PHOTO_FEE

    print( TOTAL_COST_MSG.format(fee)) 

else:
    print(f'Sorry, you are too short for this ride.  Next time wear shoes that add {MIN_HEIGHT - height} cm.')

print('='*80)
