import re
from src.models.restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""
    vazio = 0
    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=flavors_list

    # MELHORIA: criamos a função para validar caracteres especiais usando expressão regular
    def validate_special_characters(self, valor):
       """
       :param valor name of flavor in string
       """
       regex = r"^[a-zA-ZáéíóúâêîôûãõàèìòùäëïöüçñÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙÄËÏÖÜÇÑ]+$"
       return re.match(regex, valor) is None

    # MELHORIA: criada função para retornar a lista de sabores:
    def flavors_display_list(self):
        display_flavors=""
        for index, flavor in enumerate(self.flavors):
            display_flavors += f" - {flavor}" + ("" if index == len(self.flavors) - 1 else ",\n")
        return display_flavors

    # MELHORIA: Alterar os 2 prints por return no método
    # Removido o texto: "print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")"
    def flavors_available(self):
        """
        Percorra a lista de sabores disponíveis e imprima.
        """
        if len(self.flavors) != self.vazio:
            display_flavors = self.flavors_display_list()
            return f"No momento temos os seguintes sabores de sorvete disponíveis: \n{display_flavors}"
        else:
            return "Estamos sem estoque atualmente!"

    # MELHORIA: Alterar os 3 prints por return no método
    # MELHORIA: Incluímos validação de caracteres válidos no sabor
    # BUG: corrigimos o retorno para informar o sabor, e não a lista de sabores
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.validate_special_characters(flavor) or len(flavor) == self.vazio:
            return f"Sabor informado: {flavor}, inválido!"
        elif len(self.flavors) == self.vazio:
            return "Estamos sem estoque atualmente!"
        elif self.flavors:
            if flavor in self.flavors:
                return (flavor)
            else:
                return f"Não temos {flavor} no momento!"

    # MELHORIA: Alterar os 3 prints por return no método.
    # MELHORIA: Inclusão do sabor no retorno de um sabor já disponível.
    # MELHORIA: Inclusão da validação de caracteres válidos no sabor.
    # BUG: Não há necessidade de validar o estoque para adicionar sabor,
    # remover if self.flavors e o return "Estamos sem estoque atualmente!"
    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if len(flavor) == self.vazio or self.validate_special_characters(flavor):
            return f"Sabor informado: {flavor}, inválido!"

        if flavor in self.flavors:
            return f"Sabor {flavor}, já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"