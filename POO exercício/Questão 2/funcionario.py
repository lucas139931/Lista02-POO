from abc import ABC, abstractmethod


class Funcionario(ABC):
    """
    Classe abstrata base da hierarquia de funcionários.
    Define o contrato que todas as subclasses devem cumprir:
    obrigatoriamente implementar calcular_pagamento().
    """

    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self) -> None:
        """Método concreto: exibe os dados comuns de qualquer funcionário."""
        print(f"  Nome : {self.nome}")
        print(f"  CPF  : {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self) -> float:
        """
        Método abstrato: cada subclasse define sua própria
        regra de cálculo de pagamento.
        """
        ...
