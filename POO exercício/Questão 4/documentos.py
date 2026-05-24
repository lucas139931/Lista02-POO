"""
Nenhuma dessas classes herda de Imprimivel.
Elas são compatíveis com o protocolo apenas por possuírem imprimir().
Isso é o duck typing estático do Python: a estrutura importa, não a herança.
"""


class Boleto:
    """
    Representa um boleto bancário imprimível.
    Atributos: codigo, valor.
    """

    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print("  ┌─────────────────────────────────────┐")
        print("  │           🧾 BOLETO BANCÁRIO         │")
        print("  ├─────────────────────────────────────┤")
        print(f"  │  Código : {self.codigo:<27}│")
        print(f"  │  Valor  : R$ {self.valor:<24,.2f}│")
        print("  └─────────────────────────────────────┘")


class Etiqueta:
    """
    Representa uma etiqueta de envio imprimível.
    Atributos: destinatario, endereco.
    """

    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print("  ┌─────────────────────────────────────┐")
        print("  │           📦 ETIQUETA DE ENVIO       │")
        print("  ├─────────────────────────────────────┤")
        print(f"  │  Para    : {self.destinatario:<27}│")
        print(f"  │  Endereço: {self.endereco:<27}│")
        print("  └─────────────────────────────────────┘")


class RelatorioSimples:
    """
    Representa um relatório textual imprimível.
    Atributo: titulo.
    """

    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo

    def imprimir(self) -> None:
        borda = "─" * 39
        print(f"  ┌{borda}┐")
        print(f"  │       📄 RELATÓRIO                    │")
        print(f"  ├{borda}┤")
        print(f"  │  {self.titulo:<37}│")
        print(f"  ├{borda}┤")
        # quebra conteudo em linhas de 37 chars
        for i in range(0, len(self.conteudo), 37):
            linha = self.conteudo[i:i+37]
            print(f"  │  {linha:<37}│")
        print(f"  └{borda}┘")
