import socket

ip = "localhost"
porto = 5000

print("Server a ligar...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, porto))

s.listen(20)

while True:
    try:
        c, addr = s.accept()
        print("Mensagem addr: ", addr)
        
        msg = c.recv(1024)
        print("mensagem c: ", msg)

        resposta = "Tun tun ATEC!"
        c.send(resposta.encode())
    except:
        print("Deu merda")