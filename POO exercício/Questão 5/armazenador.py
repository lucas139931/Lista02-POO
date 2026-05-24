"""
PARTE A — Abordagem com ABC
============================
Contrato por HERANÇA: as subclasses devem obrigatoriamente
herdar de Armazenador e implementar salvar().
O Python verifica esse contrato em tempo de instanciação.
"""

from abc import ABC, abstractmethod


class Armazenador(ABC):
    """
    Superclasse abstrata da hierarquia formal de armazenamento.
    Define o contrato que todas as implementações devem cumprir.
    Não pode ser instanciada diretamente.
    """

    @abstractmethod
    def salvar(self, dado: str) -> None:
        """Persiste o dado no destino específico da subclasse."""
        ...


class ArmazenadorArquivo(Armazenador):
    """
    Persiste dados em um arquivo local no sistema de arquivos.
    Herda de Armazenador — vínculo formal e explícito.
    """

    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def salvar(self, dado: str) -> None:
        print(f"  💾 [ARQUIVO]  → {self.caminho_arquivo}")
        print(f"     Salvando  : \"{dado}\"")
        print(f"     Status    : gravado em disco com sucesso.")


class ArmazenadorBanco(Armazenador):
    """
    Persiste dados em um banco de dados relacional.
    Herda de Armazenador — vínculo formal e explícito.
    """

    def __init__(self, nome_banco: str, tabela: str):
        self.nome_banco = nome_banco
        self.tabela = tabela

    def salvar(self, dado: str) -> None:
        print(f"  🗄️  [BANCO]    → {self.nome_banco} / tabela '{self.tabela}'")
        print(f"     Salvando  : \"{dado}\"")
        print(f"     Status    : INSERT executado com sucesso.")
