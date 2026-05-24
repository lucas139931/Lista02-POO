from notificador import Notificador


class CentralNotificacoes:
    """
    Gerencia todos os canais de notificação cadastrados.
    enviar_para_todos() demonstra polimorfismo: chama notificar()
    em cada objeto sem precisar saber qual canal está sendo usado.
    """

    def __init__(self):
        self._notificadores: list[Notificador] = []

    def adicionar_notificador(self, notificador: Notificador) -> None:
        """Registra um novo canal na central."""
        if not isinstance(notificador, Notificador):
            raise TypeError("Apenas objetos do tipo Notificador são aceitos.")
        self._notificadores.append(notificador)
        print(f"  ✔ {type(notificador).__name__} registrado com sucesso.")

    def enviar_para_todos(self, mensagem: str) -> None:
        """
        Percorre todos os canais e chama notificar() em cada um.
        Polimorfismo em ação: o comportamento varia conforme
        o tipo real do objeto — sem if/elif.
        """
        total = len(self._notificadores)
        print(f"\n{'='*50}")
        print(f"  📣 Disparando para {total} canal(is)...")
        print(f"{'='*50}\n")

        if not self._notificadores:
            print("  Nenhum notificador cadastrado.")
            return

        for notificador in self._notificadores:
            notificador.notificar(mensagem)   # ← polimorfismo aqui
            print()

        print(f"{'='*50}")
        print(f"  ✅ Mensagem enviada para todos os {total} canal(is).")
        print(f"{'='*50}\n")
