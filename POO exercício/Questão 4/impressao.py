from imprimivel import Imprimivel


def processar_impressao(item: Imprimivel) -> None:
    """
    Recebe qualquer objeto compatível com o protocolo Imprimivel
    e delega a impressão para o método imprimir() do próprio objeto.

    O type hint 'Imprimivel' é um contrato para o type checker (mypy/pyright):
    garante em análise estática que 'item' possui imprimir().
    Em tempo de execução, o Python usa duck typing normalmente.
    """
    item.imprimir()
