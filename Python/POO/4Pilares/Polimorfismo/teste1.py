#classe pai
class Aplicativo:
    def enviar_mensagem(self):
        #metodo generico: apenas um modelo
        print ("Mensagem enviada")



class Whatsapp(Aplicativo):
    def enviar_mensagem(self):
        #Sobrescreve o método da classe base
        print ("Mensagem enviada pelo zap")

class Instagram(Aplicativo):
    def enviar_mensagem(self):
        #Cada classe filha implementa o metodo de forma diferente
        print ("Mensagem enviada pelo Instagram")

class Email(Aplicativo):
    def enviar_mensagem(self):
        print ("Mensagem enviada pelo email")

class Messenger(Aplicativo):
    def enviar_mensagem(self):
        print ("Mensagem enviada pelo Messenger")

#testando polimorfismo
apps = [Whatsapp(), Instagram(), Email(), Messenger()]
for app in apps:
    #O mesmo metodo 'enviar_mensagem' gera resultados diferentes
    app.enviar_mensagem()
