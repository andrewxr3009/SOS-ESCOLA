
import tkinter as tk
from tkinter import messagebox
import telebot

# Inicializando o bot do Telegram
TOKEN = '5915708120:AAGxi2W00UfD30p3OaKtERTWagKT7KV6i6Y'
bot = telebot.TeleBot(TOKEN)

# Função para enviar mensagem de SOS
def enviar_mensagem_sos():
    print("Função enviar_mensagem_sos concluída")
    mensagem = "🆘 ATENÇÃO 🆘 A Escola está sob ataque"
    bot.send_message(CHAT_ID, mensagem)
    messagebox.showinfo("Mensagem de SOS", "Mensagem de SOS enviada com sucesso!")

# Função para tratar o clique do botão SOS
def clicar_botao_sos():
    print("Função clicar_botao_sos concluída")
    enviar_mensagem_sos()

# Função para criar a interface gráfica
def criar_interface_grafica():
    print("Função criar_interface_grafica concluída")
    root = tk.Tk()
    root.title("SOS Escola")
    root.geometry("200x100")

    btn_sos = tk.Button(root, text="SOS", command=clicar_botao_sos)
    btn_sos.pack()

    root.mainloop()

# Função para rodar o bot
def run_bot():
    print("Função run_bot concluída")
    bot.polling()

# Configurar o ID do chat do grupo do Telegram
CHAT_ID = '-1001927736438'

# Iniciando a interface gráfica e o bot
criar_interface_grafica()
run_bot()
