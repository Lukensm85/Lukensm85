def calculate_next_months_food(dogs_by_size_list, left_over_food):
    '''
    dogs_by_size_list: order number of dogs must be small-medium-large
    '''

    small_dog_amount = dogs_by_size_list[0]
    medium_dog_amount = dogs_by_size_list[1]
    large_dog_amount = dogs_by_size_list[2]
    
    #food per dog in lbs:
    s_food = 10
    m_food = 20
    l_food = 30
    
    food_to_order = (small_dog_amount * s_food) + (medium_dog_amount * m_food) + (large_dog_amount * l_food)
    food_to_order -= left_over_food
    food_to_order *= 1.2
    #food_to_order = round(food_to_order, 0)
    
    return food_to_order
    
print(calculate_next_months_food([5, 7, 8], 12))