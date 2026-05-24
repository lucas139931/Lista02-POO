"""
main.py — Sistema de Armazenamento: ABC vs Protocol
=====================================================
Compara lado a lado as duas abordagens no mesmo problema.

  PARTE A  →  ABC       contrato por HERANÇA (rígido, verificado em runtime)
  PARTE B  →  Protocol  contrato ESTRUTURAL  (flexível, verificado staticamente)
  PARTE C  →  Funções   mostram qual abordagem aceita qual objeto
"""

from armazenador import ArmazenadorArquivo, ArmazenadorBanco, Armazenador
from salvavel import ArmazenadorNuvem
from funcoes import executar_salvamento_formal, executar_salvamento_flexivel


DADO = "{'usuario': 'ana.souza', 'acao': 'login', 'ts': '2026-05-22T10:00:00'}"

LINE = "=" * 54


def titulo(texto: str) -> None:
    print(f"\n{LINE}")
    print(f"  {texto}")
    print(LINE)


def subtitulo(texto: str) -> None:
    print(f"\n  ── {texto} {'─' * (48 - len(texto))}")


def main() -> None:

    # ── Criar os objetos ──────────────────────────────────────────────────
    arquivo = ArmazenadorArquivo("/var/log/app/eventos.log")
    banco   = ArmazenadorBanco("postgres_prod", "eventos")
    nuvem   = ArmazenadorNuvem("empresa-dados-prod", "sa-east-1")


    # ─────────────────────────────────────────────────────────────────────
    # PARTE A — Função FORMAL (ABC): só aceita hierarquia Armazenador
    # ─────────────────────────────────────────────────────────────────────
    titulo("PARTE A — executar_salvamento_formal()  [ABC]")

    subtitulo("ArmazenadorArquivo (herda de Armazenador)")
    print()
    executar_salvamento_formal(arquivo, DADO)

    subtitulo("ArmazenadorBanco (herda de Armazenador)")
    print()
    executar_salvamento_formal(banco, DADO)

    subtitulo("ArmazenadorNuvem → NÃO herda: deve falhar")
    print()
    try:
        executar_salvamento_formal(nuvem, DADO)   # type: ignore
    except TypeError as e:
        print(f"  ❌ Erro esperado : {e}")
        print("  ✔  Função formal rejeita quem não pertence à hierarquia ABC.")


    # ─────────────────────────────────────────────────────────────────────
    # PARTE B — Função FLEXÍVEL (Protocol): aceita qualquer um com salvar()
    # ─────────────────────────────────────────────────────────────────────
    titulo("PARTE B — executar_salvamento_flexivel()  [Protocol]")

    subtitulo("ArmazenadorArquivo (tem salvar() → compatível)")
    print()
    executar_salvamento_flexivel(arquivo, DADO)

    subtitulo("ArmazenadorBanco (tem salvar() → compatível)")
    print()
    executar_salvamento_flexivel(banco, DADO)

    subtitulo("ArmazenadorNuvem (tem salvar() → compatível!)")
    print()
    executar_salvamento_flexivel(nuvem, DADO)

    subtitulo("Classe externa sem herança (duck typing puro)")
    print()

    class LoggerExterno:
        """Simula uma lib externa que também tem salvar() por coincidência."""
        def salvar(self, dado: str) -> None:
            print(f"  📡 [LOGGER EXTERNO] → transmitindo dado para monitor...")
            print(f"     Dado : \"{dado[:40]}...\"")

    executar_salvamento_flexivel(LoggerExterno(), DADO)
    print("  ✔  Aceito sem herdar nada — apenas por ter salvar().")


    # ─────────────────────────────────────────────────────────────────────
    # PARTE C — Quadro comparativo lado a lado
    # ─────────────────────────────────────────────────────────────────────
    titulo("PARTE C — Comparativo: o que cada abordagem aceita")

    objetos = [
        ("ArmazenadorArquivo", arquivo,  True,  True),
        ("ArmazenadorBanco",   banco,    True,  True),
        ("ArmazenadorNuvem",   nuvem,    False, True),
        ("LoggerExterno",      LoggerExterno(), False, True),
    ]

    print(f"\n  {'Objeto':<25} {'Formal (ABC)':<16} {'Flexível (Protocol)'}")
    print(f"  {'─'*24} {'─'*15} {'─'*20}")

    for nome, obj, aceita_formal, aceita_flexivel in objetos:
        f_str = "✅ aceita" if aceita_formal  else "❌ rejeita"
        p_str = "✅ aceita" if aceita_flexivel else "❌ rejeita"
        print(f"  {nome:<25} {f_str:<16} {p_str}")

    print(f"\n  {'─'*54}")

    # ── Provar que Armazenador não pode ser instanciado ───────────────────
    subtitulo("ABC impede instanciação direta")
    print()
    try:
        a = Armazenador()
    except TypeError as e:
        print(f"  ❌ Erro esperado : {e}")
        print("  ✔  ABC protege o contrato em tempo de instanciação.\n")

    print(LINE)


if __name__ == "__main__":
    main()
