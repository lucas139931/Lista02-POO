from funcionario import Funcionario


class FuncionarioAssalariado(Funcionario):
    """
    Funcionário com salário fixo mensal.
    Pagamento = salario_mensal (valor fixo, independente de horas ou vendas).
    """

    def __init__(self, nome: str, cpf: str, salario_mensal: float):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def mostrar_dados(self) -> None:
        print("[💼 Assalariado]")
        super().mostrar_dados()
        print(f"  Salário Mensal : R$ {self.salario_mensal:,.2f}")

    def calcular_pagamento(self) -> float:
        """Retorna diretamente o salário fixo mensal."""
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    """
    Funcionário remunerado por hora trabalhada.
    Pagamento = horas_trabalhadas × valor_hora
    """

    def __init__(self, nome: str, cpf: str,
                 horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def mostrar_dados(self) -> None:
        print("[⏱  Horista]")
        super().mostrar_dados()
        print(f"  Horas Trabalhadas : {self.horas_trabalhadas}h")
        print(f"  Valor por Hora    : R$ {self.valor_hora:,.2f}")

    def calcular_pagamento(self) -> float:
        """Pagamento proporcional às horas efetivamente trabalhadas."""
        return self.horas_trabalhadas * self.valor_hora


class FuncionarioComissionado(Funcionario):
    """
    Funcionário remunerado por comissão sobre vendas.
    Pagamento = total_vendas × (percentual_comissao / 100)
    """

    def __init__(self, nome: str, cpf: str,
                 total_vendas: float, percentual_comissao: float):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao  # ex.: 8.5 para 8,5%

    def mostrar_dados(self) -> None:
        print("[📈 Comissionado]")
        super().mostrar_dados()
        print(f"  Total em Vendas     : R$ {self.total_vendas:,.2f}")
        print(f"  Percentual Comissão : {self.percentual_comissao}%")

    def calcular_pagamento(self) -> float:
        """Pagamento baseado no volume de vendas e na taxa de comissão."""
        return self.total_vendas * (self.percentual_comissao / 100)
