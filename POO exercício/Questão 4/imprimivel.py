from typing import Protocol


class Imprimivel(Protocol):
    """
    Contrato estrutural do sistema de impressão.

    Qualquer classe que possua o método imprimir() é automaticamente
    compatível com este protocolo — sem precisar herdar explicitamente.
    Isso é chamado de duck typing estático: "se tem imprimir(), é imprimível."
    """

    def imprimir(self) -> None:
        """Exibe o conteúdo do objeto no canal de impressão."""
        ...
