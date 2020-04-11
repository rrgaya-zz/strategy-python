

class Default:

    def calculate(self, order):
        return order.value * 0.05


class Express:
    
    def calculate(self, order):
        return order.value * 0.1



# Exemplo usando funções


# def calculate_default(order):
#     return order.value * 0.05

# def calculate_express(order):
#     return order.value * 0.1