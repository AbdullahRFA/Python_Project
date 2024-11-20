## inout
# total rent
# total food ordered for snacking
# electricity units spent
# charge per electricity unit

##output
# total amount you've to pay

def calculation(total_rent,elect_unit,charge_per_unit,total_food_cost,number_of_people):
    """
    This Python function calculates the amount each person has to pay for rent, electricity, and food expenses based on the total costs and number of people sharing the expenses.
    
    :param total_rent: The `total_rent` parameter represents the total rent for the hoster/flat
    :param elect_unit: The `elect_unit` parameter in the `calculation` function represents the total units of electricity consumed. This value is used to calculate the total electricity bill by multiplying it with the `charge_per_unit` rate
    :param charge_per_unit: The `charge_per_unit` parameter in the `calculation` function represents the cost per unit of electricity consumed. This value is used to calculate the total electricity bill based on the total units of electricity consumed (`elect_unit`)
    :param total_food_cost: The `total_food_cost` parameter in the `calculation` function represents the total cost of food for the month. This could include groceries, dining out, or any other food-related expenses incurred during the month
    :param number_of_people: The `number_of_people` parameter in the `calculation` function represents the total number of individuals sharing the expenses for rent, electricity, and food costs. This parameter is used to calculate the total cost of the month and then divide it by the number of people to determine the amount each person needs
    :return: The function `calculation` is returning the total cost of a month divided by the number of people staying together.
    """
    total_electricity_bil = elect_unit*charge_per_unit
    total_cost_of_a_month = total_electricity_bil+total_rent+total_food_cost
    return total_cost_of_a_month/number_of_people
    


total_rent = float(input("Enter your hoster/flat total rent : "))
elect_unit = float(input("Enter total unit of electricity spent : "))
charge_per_unit =float(input("Enter charge per unit : "))
total_food_cost = float(input("Enter total food cost : "))
number_of_people = int(input("Enter the number of person stay together : "))
amount_to_pay = calculation(total_rent,elect_unit,charge_per_unit,total_food_cost,number_of_people)
print("\nYou have to pay for this month : ",amount_to_pay,'\n')