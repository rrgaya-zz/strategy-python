from strategy.shipping import Default, Express
from strategy.order import Order
from strategy.calcute_shipping import CalculateShipping



def main():
    order = Order(500)
    calculate_shipping = CalculateShipping()
    try:
        calculate_shipping.execute_calculation(order, Default())
        calculate_shipping.execute_calculation(order, Express())
    except ValueError as e:
        print(f"Erro ao tentar calcular o frete - {e}")


if __name__ == "__main__":
    main()