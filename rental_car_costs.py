
def rental_car_cost(days):
    aluguel = 40 * days
    if days >= 7:
       return aluguel * 40 - 50
    elif days >= 3 and days < 7:
        return aluguel * 40 - 20
    else:
        return aluguel
        
print (rental_car_cost(8))
