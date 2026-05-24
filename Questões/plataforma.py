from midia import Midia


class Plataforma:
    """
    Plataforma educacional que armazena e gerencia mídias.
    Demonstra polimorfismo ao chamar reproduzir() em cada objeto
    sem precisar saber qual subclasse está sendo usada.
    """

    def __init__(self, nome: str):
        self.nome = nome
        self._midias: list[Midia] = []

    def adicionar_midia(self, midia: Midia) -> None:
        """Adiciona uma mídia à plataforma."""
        if not isinstance(midia, Midia):
            raise TypeError("Apenas objetos do tipo Midia podem ser adicionados.")
        self._midias.append(midia)
        print(f"  ✔ '{midia.titulo}' adicionado(a) com sucesso.")

    def listar_midias(self) -> None:
        """Lista todas as mídias cadastradas com seus detalhes."""
        print(f"\n{'='*50}")
        print(f"  Plataforma: {self.nome}")
        print(f"  Total de mídias: {len(self._midias)}")
        print(f"{'='*50}")
        if not self._midias:
            print("  Nenhuma mídia cadastrada.")
            return
        for i, midia in enumerate(self._midias, start=1):
            print(f"\n  [{i}]", end=" ")
            midia.mostrar_info()
        print(f"{'='*50}\n")

    def reproduzir_todas(self) -> None:
        """
        Percorre a lista e chama reproduzir() em cada mídia.
        Polimorfismo em ação: o comportamento varia conforme
        o tipo real do objeto, sem condicionais explícitos.
        """
        print(f"\n{'='*50}")
        print(f"  ▶  Reproduzindo todas as mídias — {self.nome}")
        print(f"{'='*50}")
        if not self._midias:
            print("  Nenhuma mídia para reproduzir.")
            return
        for midia in self._midias:
            midia.reproduzir()
        print(f"{'='*50}")
        print(f"  ✅ Reprodução concluída ({len(self._midias)} mídia(s)).\n")
