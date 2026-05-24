"""
PARTE C — Funções de salvamento
=================================
Duas funções com assinaturas diferentes revelam a diferença
entre as abordagens: uma exige herança, a outra aceita estrutura.
"""

from armazenador import Armazenador
from salvavel import Salvavel


def executar_salvamento_formal(armazenador: Armazenador, dado: str) -> None:
    """
    Trabalha apenas com objetos da hierarquia ABC.
    O type hint 'Armazenador' sinaliza: só aceita quem
    herdou formalmente e implementou salvar().

    Tenta usar isinstance() para reforçar o contrato em runtime.
    """
    if not isinstance(armazenador, Armazenador):
        raise TypeError(
            f"'{type(armazenador).__name__}' não pertence à hierarquia "
            f"de Armazenador. Use executar_salvamento_flexivel() para "
            f"objetos fora da hierarquia ABC."
        )
    armazenador.salvar(dado)


def executar_salvamento_flexivel(objeto: Salvavel, dado: str) -> None:
    """
    Trabalha com qualquer objeto compatível com Salvavel.
    Não importa de onde vem o objeto — ABC, Protocol, lib externa,
    classe anônima — desde que tenha salvar(), funciona.
    """
    objeto.salvar(dado)
