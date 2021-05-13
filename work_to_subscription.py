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

if __name__ == '__main__':
    """
    Say, if I work at McDonald's, I'd get paid $8.45 / hour.
    And I want to pay a subscription to Adobe Illustrator at $20.99 / month.
    How much Time do I need to spend so that the time is not wasted?
    """
    conversion(8.45, 20.99)
    """
    would result in "2 hour 29 minute 3 second" and it returns (2, 29, 3) as a tuple
    """
