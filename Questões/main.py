"""
main.py — Ponto de entrada do Sistema de Mídias Educacionais
=============================================================
Demonstra:
  • hierarquia de classes (Video, Podcast, TextoNarrado → Midia)
  • polimorfismo via reproduzir_todas()
  • uso da classe abstrata como contrato
"""

from midias import Video, Podcast, TextoNarrado
from plataforma import Plataforma


def main() -> None:
    # ── 1. Criar a plataforma ─────────────────────────────────────────────
    plataforma = Plataforma("EduLearn +")

    # ── 2. Criar as mídias ────────────────────────────────────────────────
    video1 = Video(
        titulo="Introdução à Programação Orientada a Objetos",
        duracao=45.0,
        resolucao="1080p"
    )

    video2 = Video(
        titulo="Estruturas de Dados: Listas e Pilhas",
        duracao=38.5,
        resolucao="4K"
    )

    podcast1 = Podcast(
        titulo="Boas Práticas em Python",
        duracao=62.0,
        apresentador="Ana Lima"
    )

    podcast2 = Podcast(
        titulo="Carreira em Tecnologia: Por onde começar?",
        duracao=55.0,
        apresentador="Carlos Mendes"
    )

    texto1 = TextoNarrado(
        titulo="Conceitos de Algoritmos para Iniciantes",
        duracao=20.0,
        idioma="Português"
    )

    texto2 = TextoNarrado(
        titulo="Clean Code: Escrevendo Código Legível",
        duracao=30.0,
        idioma="Inglês"
    )

    # ── 3. Adicionar à plataforma ─────────────────────────────────────────
    print("\n📥 Adicionando mídias à plataforma...")
    for midia in [video1, video2, podcast1, podcast2, texto1, texto2]:
        plataforma.adicionar_midia(midia)

    # ── 4. Listar as mídias ───────────────────────────────────────────────
    plataforma.listar_midias()

    # ── 5. Reproduzir todas (polimorfismo) ────────────────────────────────
    plataforma.reproduzir_todas()

    # ── 6. Demonstrar que Midia não pode ser instanciada diretamente ──────
    print("─" * 50)
    print("Tentando instanciar Midia diretamente...")
    try:
        from midia import Midia
        m = Midia("Teste", 10)          # deve lançar TypeError
    except TypeError as e:
        print(f"  ❌ Erro esperado: {e}")
        print("  ✔  Correto! Classes abstratas não podem ser instanciadas.")
    print("─" * 50)


if __name__ == "__main__":
    main()
