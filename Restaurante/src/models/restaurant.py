class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    # MELHORIA: Alterar os 2 prints por return no método.
    # BUG: frase com a palavra errada "restaturante"
    # BUG: exibe o tipo de cozinha no lugar do nome do restaurante
    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        if self.restaurant_name == "" or self.cuisine_type == "":
            return "Restaurante ou tipo de cozinha desconhecidos!"
        else:
            return f"Esse restaurante chama {self.restaurant_name} and serve {self.cuisine_type}. Esse restaturante está servindo {self.number_served} consumidores desde que está aberto"


    # MELHORIA: Alterar os 2 prints por return no método.
    # BUG: correção do self.open = False para True para indicar que o restaurante agora está aberto
    # BUG: correção no número atendido self.number_served = -2 para zero.
    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    # MELHORIA: Alterar os 2 prints por return no método.
    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    # MELHORIA: Alterar o print do else por return no método.
    # MELHORIA: Incluir validação para números negativos de pessoas atendidas
    # BUG: não tem retorno o if com o número total de pessoas atendidas
    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if total_customers >= 0:
            if self.open:
                self.number_served = total_customers
                return f"Total de pessoas atendidas: {total_customers}"
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return f"Total de pessoas atendidas: {total_customers}, inválido!"


    # MELHORIA: Alterar o print do else por return no método.
    # MELHORIA: Incluir validação para números negativos de pessoas atendidas
    # BUG: não tem retorno do primeiro if com o aumento do número total de clientes atendidos por este restaurante.
    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if more_customers > 0:
            if self.open:
                self.number_served += more_customers
                return f"Total de clientes atendidos por este restaurante: {self.number_served}"
            else:
                return f"{self.restaurant_name} está fechado!"
        else:
            return f"O valor de aumento de clientes atendidos: {more_customers}, é inválido!"