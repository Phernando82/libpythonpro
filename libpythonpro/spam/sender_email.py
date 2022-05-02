class Sender:
    def send(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass