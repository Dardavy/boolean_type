Colors = ['blue', 'red', 'white', 'champagne', 'orange']
Fruits = ['cherry', 'tangerine','orange', 'apple', 'banana']
Phone = ['apple', 'infinix','orange','samsung', 'tecno']
Drinks = ['vodka', 'orange','champagne', 'whiskey', 'liquor']

common_elements = set(Colors).intersection(Fruits,Phone,Drinks)

def cohort_four():
    if common_elements:
        print('True!', 'The common elements are', common_elements)
    else:
        print('False!', 'There are no common elements')

        
cohort_four()