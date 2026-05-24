from funcionario import Funcionario


class Empresa:
    """
    Armazena e gerencia os funcionários da empresa.
    mostrar_folha_pagamento() demonstra polimorfismo: chama
    calcular_pagamento() sem saber qual subclasse está sendo usada.
    """

    def __init__(self, nome: str):
        self.nome = nome
        self._funcionarios: list[Funcionario] = []

    # ── Gestão de funcionários ─────────────────────────────────────────────

    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
        """Valida o tipo e registra o funcionário na empresa."""
        if not isinstance(funcionario, Funcionario):
            raise TypeError("Apenas objetos do tipo Funcionario são aceitos.")
        self._funcionarios.append(funcionario)
        print(f"  ✔ {funcionario.nome} adicionado(a) com sucesso.")

    # ── Relatórios ─────────────────────────────────────────────────────────

    def listar_funcionarios(self) -> None:
        """Exibe os dados completos de todos os funcionários cadastrados."""
        print(f"\n{'='*52}")
        print(f"  Empresa : {self.nome}")
        print(f"  Total de funcionários: {len(self._funcionarios)}")
        print(f"{'='*52}")

        if not self._funcionarios:
            print("  Nenhum funcionário cadastrado.")
            return

        for i, func in enumerate(self._funcionarios, start=1):
            print(f"\n  [{i}] ", end="")
            func.mostrar_dados()

        print(f"\n{'='*52}\n")

    def mostrar_folha_pagamento(self) -> None:
        """
        Percorre a lista e chama calcular_pagamento() em cada funcionário.
        Polimorfismo: o mesmo método produz resultados diferentes
        dependendo do tipo real do objeto — sem nenhum if/elif.
        """
        print(f"\n{'='*52}")
        print(f"  💰 FOLHA DE PAGAMENTO — {self.nome}")
        print(f"{'='*52}")

        if not self._funcionarios:
            print("  Nenhum funcionário para calcular.")
            return

        total_geral = 0.0

        for func in self._funcionarios:
            pagamento = func.calcular_pagamento()   # ← polimorfismo aqui
            total_geral += pagamento
            print(f"  {func.nome:<30} R$ {pagamento:>10,.2f}")

        print(f"{'─'*52}")
        print(f"  {'TOTAL A PAGAR':<30} R$ {total_geral:>10,.2f}")
        print(f"{'='*52}\n")
