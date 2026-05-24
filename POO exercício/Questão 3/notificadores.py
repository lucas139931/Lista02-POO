from notificador import Notificador


class NotificadorEmail(Notificador):
    """
    Envia notificações por e-mail.
    Atributo: endereco_email — destinatário da mensagem.
    """

    def __init__(self, endereco_email: str):
        self.endereco_email = endereco_email

    def notificar(self, mensagem: str) -> None:
        print(f"  📧 [E-MAIL] → {self.endereco_email}")
        print(f"     Mensagem : {mensagem}")


class NotificadorSMS(Notificador):
    """
    Envia notificações por SMS.
    Atributo: numero_telefone — número de destino.
    """

    def __init__(self, numero_telefone: str):
        self.numero_telefone = numero_telefone

    def notificar(self, mensagem: str) -> None:
        print(f"  📱 [SMS] → {self.numero_telefone}")
        print(f"     Mensagem : {mensagem}")


class NotificadorApp(Notificador):
    """
    Envia notificações via push no aplicativo.
    Atributo: nome_usuario — identificador do usuário no app.
    """

    def __init__(self, nome_usuario: str):
        self.nome_usuario = nome_usuario

    def notificar(self, mensagem: str) -> None:
        print(f"  🔔 [APP] → @{self.nome_usuario}")
        print(f"     Mensagem : {mensagem}")
