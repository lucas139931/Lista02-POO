from abc import ABC, abstractmethod


class Notificador(ABC):
    """
    Contrato formal do sistema de notificações.
    Qualquer canal de envio DEVE implementar notificar(),
    garantindo que a CentralNotificacoes possa tratar
    todos os notificadores de forma uniforme.
    """

    @abstractmethod
    def notificar(self, mensagem: str) -> None:
        """Envia a mensagem pelo canal específico da subclasse."""
        ...
