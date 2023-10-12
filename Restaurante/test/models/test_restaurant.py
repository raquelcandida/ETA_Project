from src.models.restaurant import Restaurant


class TestRestaurant:
    restaurant_name = "Mokay"
    cuisine_type = "Japanese food"
    def test_describe_restaurant(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = f"Esse restaurante chama {self.restaurant_name} and serve {self.cuisine_type}. Esse restaturante está servindo 0 consumidores desde que está aberto"
        assert restaurant.describe_restaurant() == result

    def test_describe_restaurant_no_name_restaurant(self):
        self.restaurant_name = ""
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = "Restaurante ou tipo de cozinha desconhecidos!"
        assert restaurant.describe_restaurant() ==  result
    def test_describe_restaurant_no_cuisine_type(self):
        self.cuisine_type = ""
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = "Restaurante ou tipo de cozinha desconhecidos!"
        assert restaurant.describe_restaurant() ==  result
    def test_describe_restaurant_no_name_restaurant_and_cousine_type(self):
        self.restaurant_name = ""
        self.cuisine_type = ""
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = "Restaurante ou tipo de cozinha desconhecidos!"
        assert restaurant.describe_restaurant() ==  result
    def test_open_restaurant(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = f"{self.restaurant_name} agora está aberto!"
        assert restaurant.open_restaurant() == result
    def test_open_restaurant_status_close(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = f"{self.restaurant_name} agora está aberto!"
        restaurant.close_restaurant()
        assert restaurant.open_restaurant() == result
    def test_open_restaurant_status_open(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        result = f"{self.restaurant_name} já está aberto!"
        restaurant.open_restaurant()
        assert restaurant.open_restaurant() == result
    def test_close_restaurant(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        result=f"{self.restaurant_name} já está fechado!"
        assert restaurant.close_restaurant() == result
    def test_close_restaurant_status_close(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        result=f"{self.restaurant_name} já está fechado!"
        restaurant.close_restaurant()
        assert restaurant.close_restaurant() == result
    def test_close_restaurant_status_open(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        result=f"{self.restaurant_name} agora está fechado!"
        restaurant.open_restaurant()
        assert restaurant.close_restaurant() == result
    def test_set_number_served(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        result=f"{self.restaurant_name} está fechado!"
        number_served = 2
        assert restaurant.set_number_served(number_served) == result
    def test_set_number_served_restaurant_close(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        result=f"{self.restaurant_name} está fechado!"
        number_served = 3
        restaurant.close_restaurant()
        assert restaurant.set_number_served(number_served) == result
    def test_set_valid_number_served_restaurant_open(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = 4
        result=f"Total de pessoas atendidas: {number_served}"
        restaurant.open_restaurant()
        assert restaurant.set_number_served(number_served) == result
    def test_set_valid_number_served_restaurant_close(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = 8
        result=f"{self.restaurant_name} está fechado!"
        restaurant.close_restaurant()
        assert restaurant.set_number_served(number_served) == result
    def test_set_number_served_invalid_number(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = -5
        result=f"Total de pessoas atendidas: {number_served}, inválido!"
        assert restaurant.set_number_served(number_served) == result
    def test_set_number_served_invalid_number_restaurant_open(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = -7
        result=f"Total de pessoas atendidas: {number_served}, inválido!"
        restaurant.open_restaurant()
        assert restaurant.set_number_served(number_served) == result
    def test_set_number_served_invalid_number_restaurant_close(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = -6
        result=f"Total de pessoas atendidas: {number_served}, inválido!"
        restaurant.close_restaurant()
        assert restaurant.set_number_served(number_served) == result
    def test_increment_number_served(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = 2
        result = f"{self.restaurant_name} está fechado!"
        assert restaurant.increment_number_served(number_served) == result
    def test_increment_number_served_restaurant_close(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = 3
        result=f"{self.restaurant_name} está fechado!"
        restaurant.close_restaurant()
        assert restaurant.increment_number_served(number_served) == result
    def test_increment_number_served_restaurant_open(self):
        restaurant=Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = 7
        result=f"Total de clientes atendidos por este restaurante: {number_served}"
        restaurant.open_restaurant()
        assert restaurant.increment_number_served(number_served) == result
    def test_increment_invalid_number_served(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = 0
        result = f"O valor de aumento de clientes atendidos: {number_served}, é inválido!"
        assert restaurant.increment_number_served(number_served) == result
    def test_increment_invalid_number_served_restaurant_close(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = -3
        result=f"O valor de aumento de clientes atendidos: {number_served}, é inválido!"
        restaurant.close_restaurant()
        assert restaurant.increment_number_served(number_served) == result
    def test_increment_invalid_number_served_restaurant_open(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        number_served = -6
        result=f"O valor de aumento de clientes atendidos: {number_served}, é inválido!"
        restaurant.open_restaurant()
        assert restaurant.increment_number_served(-6) == result