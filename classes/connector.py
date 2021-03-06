import socket
import threading

LOGO_ASCII = " " * 11 + "*" + " " * 67 + "\n" + " " * 10 + "%," + " " * 67 + "\n" + " " * 9 + "%" + "," * 2 + "#" + " " * 66 + "\n" + " " * 8 + "(,*,*" + " " * 66 + "\n" + " " * 7 + "/" + " " * 2 + "/" + "," * 3 + " " * 19 + "#" + " " * 45 + "\n" + " " * 9 + "," * 5 + " " * 20 + "*" + " " * 44 + "\n" + " " * 7 + "%" + "," * 6 + "/" + " " * 19 + "*/" + " " * 43 + "\n" + " " * 6 + "*" + "," * 4 + "/" + "*" * 3 + "#" + " " * 18 + "(/" + "%" + " " * 5 + "." + " " * 36 + "\n" + " " * 4 + "," * 3 + "*" * 2 + "&" + " " * 2 + "/" + "*" * 3 + "%" + " " * 17 + "%" + "/" * 2 + " " * 8 + "@(" + " " * 32 + "\n" + " " * 3 + "," + "*" * 3 + "/" + " " * 5 + "#" + "*" * 3 + "#" + " " * 16 + "&" + "/" * 2 + "(" + " " * 10 + "&@" + "." + " " * 28 + "\n" + " " * 2 + "," + "*" * 3 + "%" + " " * 7 + "#" + "*" * 4 + " " * 15 + "&" + "/" * 2 + "#" + " " * 13 + "%" * 16 + "&" + " " * 11 + "\n" + " " * 2 + "*" * 3 + "(" + " " * 9 + "(" + "*" * 2 + "/" * 2 + "#" + " " * 13 + "&" + "/" * 2 + "(" + " " * 16 + "," + "%" * 8 + "&" * 4 + "%" * 2 + "@" + " " * 9 + "\n " + "*" * 3 + "," + " " * 11 + "%" + "/" * 5 + " " * 12 + "#" + "(" * 3 + " " * 15 + "(" + "#" * 11 + "%" * 8 + "&" * 2 + "(" + "," * 2 + "&\n" + "#" + "*" * 2 + "&" + " " * 13 + "(" + "/" * 5 + "%" + " " * 10 + "(" * 4 + " " * 3 + "." * 2 + " " * 3 + "%&" + "#" * 15 + ". " + "(" + "&" + "%" * 8 + "& " + "\n" + "*" * 3 + " " * 16 + "/" * 6 + "&" + " " * 7 + "." + "(" * 4 + " " * 3 + "%" + " " * 5 + "#" * 7 + "(" * 10 + "#" * 3 + "%" + " " * 11 + "\n" + "*" * 2 + "&" + " " * 17 + "(" + "/" * 3 + "(" * 3 + "&" + " " * 5 + "#" + "(" * 4 + " " * 2 + "&%" + " " * 5 + "#" * 2 + "(" * 8 + "%" + " " * 10 + "#" * 2 + "%" * 2 + " " * 5 + "\n" + "*" * 3 + " " * 19 + "%" + "(" * 6 + "%" + " " * 2 + "&" + "(" * 4 + "&" + " " * 2 + "%#" + " " * 4 + "#" + "(" * 8 + "&" + " " * 23 + "\n" + "/" * 2 + " " * 22 + "%" + "(" * 12 + " " * 2 + "%" + "#" * 2 + ", " + "(" * 7 + "/" * 2 + "(" + " " * 25 + "\n" + "/" * 2 + " " * 24 + "&" + "(" * 7 + "#" * 2 + "% " + "." + "#" * 4 + "(" * 5 + "/" * 4 + "#" + " " * 26 + "\n" + "/" * 2 + "," + " " * 25 + "(" * 2 + "#" * 6 + " " * 2 + "#" * 2 + "(" * 5 + "/" * 5 + "*" * 3 + "%" * 2 + "&" + "*" * 6 + "/" + " " * 14 + "\n(" + "/" + "%" + " " * 27 + "." + "#" * 4 + "%" + " " * 2 + "#" * 3 + "(" * 5 + "/" * 4 + "." * 2 + "&" + "*" * 3 + "/(" + " " * 4 + "@" + " " * 2 + "." + " " * 13 + "\n*" + "/" + "(" + " " * 27 + "." + "#" * 4 + " " * 2 + "#" * 4 + "(" * 4 + "/" * 3 + "(" + " " * 30 + "\n " + "(" * 2 + " " * 27 + "," + "#" * 3 + "&" + " " * 2 + "#" * 2 + "(" * 4 + "/" * 2 + "(" + " " * 31 + "\n" + " " * 2 + "(#" + " " * 26 + "." + "#" * 3 + "." + " " * 2 + "#" * 3 + "(" * 4 + "/" * 3 + " " * 32 + "\n" + " " * 2 + ".(" + "," + " " * 25 + "." + "#" * 3 + " " * 3 + "#" * 4 + "(" * 4 + "/," + " " * 32 + "\n" + " " * 3 + ",(" + " " * 26 + "%" * 3 + " " * 3 + "#" * 4 + "(" * 5 + " " * 33 + "\n" + " " * 4 + ".(" + " " * 25 + "%" * 3 + " " * 3 + "#" * 5 + "(" * 3 + "&" + " " * 2 + "," + "/" * 2 + "*." + " " * 26 + "\n" + " " * 6 + "%" + " " * 24 + "%" * 2 + "&" + " " * 3 + "%" + "#" * 4 + "(" * 5 + "/" * 6 + "*" + " " * 25 + "\n" + " " * 7 + "@" + " " * 23 + "&%" + "@" + " " * 3 + "@%" + "#" * 5 + "(" * 5 + "/" * 6 + " " * 24 + "\n" + " " * 8 + "." + " " * 22 + "#%" + "@" + " " * 4 + "%" * 2 + "#" * 5 + "(" * 4 + "," + " " * 2 + "/" * 2 + "(" + " " * 3 + "%/" + "&" + " " * 18 + "\n" + " " * 32 + "%@" + " " * 4 + "&" + "%" * 2 + "#" * 5 + "&" + " " * 6 + "(" * 2 + "%(" + "/" + "(" + " " * 20 + "\n" + " " * 32 + "&@" + " " * 5 + "%" * 4 + "#" * 3 + " " * 8 + "(" * 2 + "%" + " " * 22 + "\n" + " " * 33 + "@" + " " * 6 + "%" * 5 + "#%" + " " * 7 + "#" + " " * 24 + "\n" + " " * 33 + "&" + " " * 7 + "@" + "%" * 6 + "*" + " " * 30 + "\n" + " " * 42 + "." + "%" * 7 + "/" + " " * 28 + "\n" + " " * 44 + ".&" + "%" * 7 + "," + " " * 25 + "\n" + " " * 47 + "*&" + "%" * 8 + "(" + " " * 21 + "\n" + " " * 51 + "#" + "&" * 2 + "%" * 8 + "@(" + " " * 15 + "\n" * 2


class ClientThread(threading.Thread):

    def __init__(self, ip, port, client_socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = client_socket
        print("[+] New game on %s %s" % (self.ip, self.port,))
        self.func = lambda: None
        self.timeout = 0
        self.timeout_message = "Trop lent !\n"

    def set_options(self, func, timeout, timeout_message):
        self.func = func
        self.timeout = timeout
        self.timeout_message = timeout_message

    def run(self):
        try:
            self.socket.settimeout(self.timeout)
            self.socket.send(LOGO_ASCII.encode("utf8"))
            self.socket.send("Newbie Contest - Challenge de programmation\n\n".encode("utf8"))
            self.func(self)
        except socket.timeout:
            self.socket.send(self.timeout_message.encode("utf8"))
        finally:
            self.socket.close()


def launch(func, port, timeout, timeout_message):
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_sock.bind(("", port))

    while True:
        tcp_sock.listen(10)
        (client_socket, (ip, port)) = tcp_sock.accept()
        thread = ClientThread(ip, port, client_socket)
        thread.set_options(func, timeout, timeout_message)
        thread.start()
