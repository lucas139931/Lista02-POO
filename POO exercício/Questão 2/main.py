"""
main.py — Sistema de Funcionários de uma Empresa
=================================================
Demonstra:
  • hierarquia de classes  (subclasses → Funcionario)
  • sobrescrita             (calcular_pagamento em cada subclasse)
  • polimorfismo            (mostrar_folha_pagamento percorre a lista
                             chamando calcular_pagamento() sem if/elif)
  • uso de ABC como contrato (Funcionario não pode ser instanciado)
"""

from funcionarios import FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
from empresa import Empresa


def main() -> None:

    # ── 1. Criar a empresa ────────────────────────────────────────────────
    empresa = Empresa("TechSolve Ltda.")

    # ── 2. Criar os funcionários ──────────────────────────────────────────

    # Assalariados — recebem salário fixo
    ana    = FuncionarioAssalariado("Ana Souza",    "111.222.333-01", salario_mensal=6_500.00)
    bruno  = FuncionarioAssalariado("Bruno Lima",   "222.333.444-02", salario_mensal=4_800.00)

    # Horistas — recebem por hora trabalhada
    carla  = FuncionarioHorista("Carla Neves",  "333.444.555-03",
                                horas_trabalhadas=160, valor_hora=35.00)
    daniel = FuncionarioHorista("Daniel Rocha", "444.555.666-04",
                                horas_trabalhadas=120, valor_hora=42.50)

    # Comissionados — recebem % sobre vendas
    elena  = FuncionarioComissionado("Elena Costa",  "555.666.777-05",
                                     total_vendas=80_000.00, percentual_comissao=8.5)
    fabio  = FuncionarioComissionado("Fábio Martins","666.777.888-06",
                                     total_vendas=55_000.00, percentual_comissao=10.0)

    # ── 3. Adicionar à empresa ────────────────────────────────────────────
    print("\n📋 Registrando funcionários na empresa...")
    for funcionario in [ana, bruno, carla, daniel, elena, fabio]:
        empresa.adicionar_funcionario(funcionario)

    # ── 4. Listar funcionários ────────────────────────────────────────────
    empresa.listar_funcionarios()

    # ── 5. Mostrar folha de pagamento (polimorfismo) ───────────────────────
    empresa.mostrar_folha_pagamento()

    # ── 6. Provar que Funcionario é abstrata e não pode ser instanciada ───
    print("─" * 52)
    print("Tentando instanciar Funcionario diretamente...")
    try:
        from funcionario import Funcionario
        f = Funcionario("Teste", "000.000.000-00")
    except TypeError as e:
        print(f"  ❌ Erro esperado : {e}")
        print("  ✔  ABC impede a instanciação direta. Correto!")
    print("─" * 52)


if __name__ == "__main__":
    main()
