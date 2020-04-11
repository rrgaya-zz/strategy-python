from shipping import Default, Express
from order import Order
from calcute_shipping import CalculateShipping


order = Order(500)
calculate_shipping = CalculateShipping()


calculate_shipping.execute_calculation(order, Default())
calculate_shipping.execute_calculation(order, Express())