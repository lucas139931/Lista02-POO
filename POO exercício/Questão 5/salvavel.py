"""
PARTE B — Abordagem com Protocol
==================================
Contrato ESTRUTURAL: qualquer classe que possua salvar(dado)
é automaticamente compatível — sem herdar nada.
O Python verifica apenas a presença do método, não a árvore de herança.
"""

from typing import Protocol


class Salvavel(Protocol):
    """
    Protocolo de contrato estrutural.
    Qualquer objeto com salvar(dado) satisfaz este protocolo,
    independente de herança — inclusive classes de libs externas.
    """

    def salvar(self, dado: str) -> None:
        """Persiste o dado de alguma forma."""
        ...


class ArmazenadorNuvem:
    """
    Persiste dados em um serviço de nuvem.
    NÃO herda de Armazenador nem de Salvavel —
    é compatível com o protocolo apenas por ter salvar().
    """

    def __init__(self, bucket: str, regiao: str):
        self.bucket = bucket
        self.regiao = regiao

    def salvar(self, dado: str) -> None:
        print(f"  ☁️  [NUVEM]    → bucket '{self.bucket}' ({self.regiao})")
        print(f"     Salvando  : \"{dado}\"")
        print(f"     Status    : upload concluído com sucesso.")
