import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        """Verifica se o servidor Urban Routes está acessível."""
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes.")
        else:
            print(
                "Não foi possível conectar ao Urban Routes. "
                "Verifique se o servidor está ligado e em execução."
            )

    def test_urban_routes(self):
        """Define a rota para o teste."""
        print("Função criada para definir a rota.")
        # Adicionar a lógica da rota na etapa S8.

    def test_order_2_ice_creams(self):
        """Adiciona dois sorvetes ao pedido."""
        number_of_ice_creams = 2

        for count in range(number_of_ice_creams):
            print(f"Adicionando sorvete {count + 1} de {number_of_ice_creams}.")
            # Adicionar a lógica para incluir um sorvete na etapa S8.

