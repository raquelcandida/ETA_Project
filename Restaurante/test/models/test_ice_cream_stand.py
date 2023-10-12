from src.models.ice_cream_stand import IceCreamStand
import unittest
import pytest
class TestIceCreamStand:
    restaurant_name = "Gelatto"
    cuisine_type = "Sorveteria"
    flavor_list = [
        "pistache",
        "coco",
        "chocolate",
        "baunilha"
    ]

    def test_flavors_available(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        result = \
        f"""No momento temos os seguintes sabores de sorvete disponíveis: 
 - pistache,
 - coco,
 - chocolate,
 - baunilha"""
        assert ice_cream.flavors_available() == result
    def test_flavors_available_empty_list(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, [])
        result = "Estamos sem estoque atualmente!"
        assert ice_cream.flavors_available() == result
    def test_flavors_display_list_empty(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, [])
        result = ""
        assert ice_cream.flavors_display_list() == result
    def test_flavors_display_list(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        result= \
        f""" - pistache,
 - coco,
 - chocolate,
 - baunilha"""
        assert ice_cream.flavors_display_list() == result
    def test_out_of_stock_flavors(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, [])
        assert ice_cream.flavors_available() == "Estamos sem estoque atualmente!"
    def test_find_flavor(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor = "chocolate"
        result = "chocolate"
        assert ice_cream.find_flavor(flavor) == result
    def test_find_flavor_not_found(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor="morango"
        result=f"Não temos {flavor} no momento!"
        assert ice_cream.find_flavor(flavor) == result
    def test_find_flavor_not_found_empty_list(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, [])
        flavor = "baunilha"
        result = "Estamos sem estoque atualmente!"
        assert ice_cream.find_flavor("morango") == result
    @pytest.mark.parametrize("value, result", [
        ("morango!", "Sabor informado: morango!, inválido!"),
        ("morango@", "Sabor informado: morango@, inválido!"),
        ("morango#", "Sabor informado: morango#, inválido!"),
        ("morango$", "Sabor informado: morango$, inválido!"),
        ("morango%", "Sabor informado: morango%, inválido!"),
        ("morango¨", "Sabor informado: morango¨, inválido!"),
        ("morango&", "Sabor informado: morango&, inválido!"),
        ("morango*", "Sabor informado: morango*, inválido!"),
        ("morango(", "Sabor informado: morango(, inválido!"),
        ("morango)", "Sabor informado: morango), inválido!"),
        ("morango_", "Sabor informado: morango_, inválido!"),
        ("morango+", "Sabor informado: morango+, inválido!"),
        ("morango{", "Sabor informado: morango{, inválido!"),
        ("morango}", "Sabor informado: morango}, inválido!"),
        ("morango[", "Sabor informado: morango[, inválido!"),
        ("morango]", "Sabor informado: morango], inválido!"),
        ("morango|", "Sabor informado: morango|, inválido!"),
        ("\\morango", "Sabor informado: \\morango, inválido!"),
        ("morango:", "Sabor informado: morango:, inválido!"),
        ("morango;", "Sabor informado: morango;, inválido!"),
       # ("mo\rango", "Sabor informado: mor\ango, inválido!"),
        ("morango<", "Sabor informado: morango<, inválido!"),
        ("morango>", "Sabor informado: morango>, inválido!"),
        ("morango?", "Sabor informado: morango?, inválido!"),
        ("morango/", "Sabor informado: morango/, inválido!")
    ])
    def test_find_flavor_invalid(self,value, result):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        assert ice_cream.find_flavor(value) == result
    def test_find_flavor_invalid_empty(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor = ""
        result = f"Sabor informado: {flavor}, inválido!"
        assert ice_cream.find_flavor(flavor) == result
    def test_add_new_flavor(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor = "morango"
        result = "morango adicionado ao estoque!"
        assert ice_cream.add_flavor(flavor) == result
    @pytest.mark.parametrize("value, result", [
        ("morango!", "Sabor informado: morango!, inválido!"),
        ("morango@", "Sabor informado: morango@, inválido!"),
        ("morango#", "Sabor informado: morango#, inválido!"),
        ("morango$", "Sabor informado: morango$, inválido!"),
        ("morango%", "Sabor informado: morango%, inválido!"),
        ("morango¨", "Sabor informado: morango¨, inválido!"),
        ("morango&", "Sabor informado: morango&, inválido!"),
        ("morango*", "Sabor informado: morango*, inválido!"),
        ("morango(", "Sabor informado: morango(, inválido!"),
        ("morango)", "Sabor informado: morango), inválido!"),
        ("morango_", "Sabor informado: morango_, inválido!"),
        ("morango+", "Sabor informado: morango+, inválido!"),
        ("morango{", "Sabor informado: morango{, inválido!"),
        ("morango}", "Sabor informado: morango}, inválido!"),
        ("morango[", "Sabor informado: morango[, inválido!"),
        ("morango]", "Sabor informado: morango], inválido!"),
        ("morango|", "Sabor informado: morango|, inválido!"),
        ("\\morango", "Sabor informado: \\morango, inválido!"),
        ("morango:", "Sabor informado: morango:, inválido!"),
        ("morango;", "Sabor informado: morango;, inválido!"),
        ("mo\rango", "Sabor informado: mo\rango, inválido!"),
        ("morango<", "Sabor informado: morango<, inválido!"),
        ("morango>", "Sabor informado: morango>, inválido!"),
        ("morango?", "Sabor informado: morango?, inválido!"),
        ("morango/", "Sabor informado: morango/, inválido!")
    ])
    def test_add_new_invalid_flavor(self, value, result):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        assert ice_cream.add_flavor(value) == result
    def test_add_new_flavor_empty(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor = ""
        result = "Sabor informado: , inválido!"
        assert ice_cream.add_flavor(flavor) == result
    def test_add_flavor_available_in_list(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor = "coco"
        result = "Sabor coco, já disponivel!"
        assert ice_cream.add_flavor(flavor) == result
    def test_add_new_flavor_added_to_stock(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavor_list)
        flavor = "manga"
        result = "manga adicionado ao estoque!"
        assert ice_cream.add_flavor(flavor) == result
    def test_add_flavor_empty_stock(self):
        ice_cream = IceCreamStand(self.restaurant_name, self.cuisine_type, [])
        flavor = "maracujá"
        result = "maracujá adicionado ao estoque!"
        assert ice_cream.add_flavor(flavor) == result