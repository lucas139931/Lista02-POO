"""
main.py — Sistema de Impressão com Protocol
============================================
Demonstra:
  • contrato estrutural via Protocol   (Imprimivel)
  • duck typing estático               (classes sem herdar de Imprimivel)
  • polimorfismo pela função           (processar_impressao chama imprimir()
                                        sem saber o tipo do objeto)
  • incompatibilidade detectável       (objeto sem imprimir() falha)
"""

from documentos import Boleto, Etiqueta, RelatorioSimples
from impressao import processar_impressao


def separador(titulo: str = "") -> None:
    if titulo:
        print(f"\n  ── {titulo} {'─' * (36 - len(titulo))}")
    else:
        print(f"\n  {'─' * 41}")


def main() -> None:

    # ── 1. Criar os documentos ────────────────────────────────────────────
    boleto = Boleto(
        codigo="34191.09008 63521.560079 27483.880000 6 93490000025000",
        valor=250.00
    )

    etiqueta = Etiqueta(
        destinatario="Maria Oliveira",
        endereco="Rua das Flores, 142 — Manaus/AM"
    )

    relatorio = RelatorioSimples(
        titulo="Resumo de Vendas — Maio/2026",
        conteudo="Total: R$ 128.450,00. Meta atingida em 102%."
    )

    # ── 2. Processar cada um via função (polimorfismo) ────────────────────
    documentos = [boleto, etiqueta, relatorio]

    print("\n" + "=" * 43)
    print("  🖨  FILA DE IMPRESSÃO")
    print("=" * 43)

    for i, doc in enumerate(documentos, start=1):
        separador(f"Documento {i} de {len(documentos)}")
        print()
        processar_impressao(doc)   # ← mesmo chamador, comportamento diferente

    separador()
    print(f"\n  ✅ {len(documentos)} documento(s) processado(s) com sucesso.\n")

    # ── 3. Provar compatibilidade estrutural sem herança ──────────────────
    separador("Teste: classe independente")
    print()

    class Certificado:
        """Classe criada do zero — sem herdar nada — mas compatível."""
        def imprimir(self) -> None:
            print("  🏅 [CERTIFICADO] Imprimindo certificado de conclusão...")

    processar_impressao(Certificado())   # funciona sem herança!
    print("  ✔  Certificado impresso sem herdar de Imprimivel.\n")

    # ── 4. Provar que objeto SEM imprimir() falha em tempo de execução ────
    separador("Teste: objeto incompatível")
    print()

    class SemImprimir:
        """Não possui o método imprimir() — incompatível com o protocolo."""
        pass

    try:
        processar_impressao(SemImprimir())  # type: ignore
    except AttributeError as e:
        print(f"  ❌ Erro esperado : {e}")
        print("  ✔  Sem imprimir(), o protocolo não é satisfeito.\n")

    print("=" * 43)


if __name__ == "__main__":
    main()
