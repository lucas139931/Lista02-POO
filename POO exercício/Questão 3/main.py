"""
main.py — Sistema de Notificações com ABC
==========================================
Demonstra:
  • contrato formal via ABC       (Notificador)
  • sobrescrita obrigatória       (notificar em cada subclasse)
  • polimorfismo                  (enviar_para_todos chama notificar()
                                   sem saber qual canal está sendo usado)
  • proteção da ABC               (instanciar Notificador diretamente falha)
  • proteção de contrato          (subclasse sem notificar() falha)
"""

from notificadores import NotificadorEmail, NotificadorSMS, NotificadorApp
from central import CentralNotificacoes


def main() -> None:

    # ── 1. Criar a central ────────────────────────────────────────────────
    central = CentralNotificacoes()

    # ── 2. Criar um notificador de cada tipo ──────────────────────────────
    email = NotificadorEmail("joao.silva@email.com")
    sms   = NotificadorSMS("+55 92 91234-5678")
    app   = NotificadorApp("joao.silva")

    # ── 3. Registrar os notificadores na central ──────────────────────────
    print("\n📋 Registrando canais na central...")
    central.adicionar_notificador(email)
    central.adicionar_notificador(sms)
    central.adicionar_notificador(app)

    # ── 4. Enviar uma mensagem para todos (polimorfismo) ──────────────────
    central.enviar_para_todos(
        "Sua assinatura foi renovada com sucesso! Validade: 22/05/2026."
    )

    # ── 5. Segundo disparo com mensagem diferente ─────────────────────────
    central.enviar_para_todos(
        "Manutenção programada: sistema indisponível das 02h às 04h."
    )

    # ── 6. Provar que Notificador é abstrata ──────────────────────────────
    print("─" * 50)
    print("Tentando instanciar Notificador diretamente...")
    try:
        from notificador import Notificador
        n = Notificador()
    except TypeError as e:
        print(f"  ❌ Erro esperado : {e}")
        print("  ✔  ABC impede a instanciação direta. Correto!")

    # ── 7. Provar que subclasse SEM notificar() também falha ──────────────
    print()
    print("Tentando criar subclasse sem implementar notificar()...")
    try:
        from notificador import Notificador

        class NotificadorIncompleto(Notificador):
            pass  # não implementa notificar()

        n = NotificadorIncompleto()
    except TypeError as e:
        print(f"  ❌ Erro esperado : {e}")
        print("  ✔  ABC exige que o contrato seja cumprido. Correto!")
    print("─" * 50)


if __name__ == "__main__":
    main()
