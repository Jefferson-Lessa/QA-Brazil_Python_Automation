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

    def test_set_route(self):
        """Define a rota para o teste."""
        print("Função criada para definir a rota.")
        #Adicionar em S8
        pass

    def test_select_plan(self):
        """Seleciona o plano de viagem."""
        print("Função criada para selecionar o plano.")
        #Adicionar em S8
        pass

    def test_fill_phone_number(self):
        """Preenche o número de telefone."""
        print("Função criada para preencher o telefone.")
        #Adicionar em S8
        pass

    def test_fill_card(self):
        """Preenche os dados do cartão."""
        print("Função criada para preencher o cartão.")
        #Adicionar em S8
        pass

    def test_comment_for_driver(self):
        """Adiciona um comentário para o motorista."""
        print("Função criada para adicionar comentário ao motorista.")
        #Adicionar em S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        """Solicita cobertor e lenços."""
        print("Função criada para solicitar cobertor e lenços.")
        #Adicionar em S8
        pass

    def test_order_2_ice_creams(self):
        """Adiciona dois sorvetes ao pedido."""
        number_of_ice_creams = 2

        for count in range(number_of_ice_creams):
            print(
                f"Adicionando sorvete {count + 1} "
                f"de {number_of_ice_creams}."
            )

        #Adicionar em S8
        pass

    def test_car_search_model_appears(self):
        """Verifica se o modelo do carro aparece."""
        print("Função criada para verificar o modelo do carro.")
        #Adicionar em S8
        pass

