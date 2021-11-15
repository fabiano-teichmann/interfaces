# Implementando interface com ABC e Protocol
Em outras linguagens de programação é comum o uso de interface, com Python em muitos caso não se faz necessário implementar
‘interfaces’, entretanto em aplicações maiores é uma ótima prática implementar uma ‘interface’. 
Nesse artigo vou demostrar como podemos implementar ‘interface’ com ABC ou protocol.

## Para rodar os testes testes você precisa install o pytest

    pip install pytest

Depois é somente rodar o pytest

    pytest
Para estudo de interface temos um cenário de envio de mensagem que pode 
ser enviado por SMS e email. Pensando que cada forma de envio e cada provedor
de envio de mensagem tem suas especificidades. Temos uma interface usando ABC e outro com o Protocol
esse exercício vem mostrar as características de cada um.

## Implementando interface com ABC
Interfaces com a biblioteca ABC é a forma mais antiga que o Protocol. Tudo o que é necessário para implementar 
essa interface


    class Dispatch(ABC):
    @abstractmethod
    def send(self) -> None:
        """Send msg"""

    @abstractmethod
    def confirm_receive(self):
        """Message can be confimed receive"""


Com a nossa classe criada a única coisa que precisamos fazer é as nossas classes DispatchEmail E DispatchSMS herdem 
dela. E elas precisam implementar os métodos send e confirm_receive