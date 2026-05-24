from abc import ABC, abstractmethod


class Midia(ABC):
    """
    Classe abstrata base para todos os tipos de mídia educacional.
    Não pode ser instanciada diretamente — serve como contrato
    para as subclasses, garantindo que reproduzir() seja implementado.
    """

    def __init__(self, titulo: str, duracao: float):
        self.titulo = titulo
        self.duracao = duracao  # duração em minutos

    def mostrar_info(self) -> None:
        """Método concreto: exibe informações gerais da mídia."""
        print(f"  Título  : {self.titulo}")
        print(f"  Duração : {self.duracao} min")

    @abstractmethod
    def reproduzir(self) -> None:
        """Método abstrato: cada subclasse define sua própria reprodução."""
        ...
