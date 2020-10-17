# coding: utf-8
from classes import connector


def game_engine(self):
    # code de l'épreuve ici
    # le paramètre contient toutes les informations pour communiquer avec le client
    #
    # Exemple :
    self.socket.send("Salut, je suis une épreuve de prog !\n".encode("utf8"))
    some_data = self.socket.recv(255).decode("utf8").strip()
    print(f"J'ai reçu : {some_data}")


# Lancer le serveur
connector.launch(
    game_engine,  # Fonction de l'épreuve
    10001,  # Port ouvert
    1,  # Temps maximal entre chaque message du client
    "Trop tard ! Vous n'avez qu'une seconde entre chaque coup !"  # Message en cas de timeout
)
