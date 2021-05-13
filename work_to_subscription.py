import math

def conversion(income_per_hour, monthly_subscription_cost):
    """
    equation: x / y = z
    where
    x = monthly subscription cost
    y = income / hour
    z = total time
    """
    total_time = monthly_subscription_cost / income_per_hour

    total_hour = math.floor(total_time)
    total_minute = math.floor(total_time * 60 % 60)
    total_second = math.ceil(total_time * 3600 % 60)    
    print(f'{total_hour} hour {total_minute} minute {total_second} second')
    
    return total_hour, total_minute, total_second
