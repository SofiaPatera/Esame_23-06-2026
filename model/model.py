from database.dao import Dao
import networkx as nx

class Model:
    def __init__(self):
        self._G = nx.Graph()
        self._users_list = []
        self.load_all_users()
        self._lista_nodi = []
        self._lista_archi = []
        self._idMappa = {}

    def load_all_users(self):
        self._users_list = Dao.read_all_users()
        print(f"Users: {self._users_list}")

    def build_graph(self, n_bus):
        self._G.clear()
        self._lista_nodi = Dao.get_nodi(n_bus)
        for n in self._lista_nodi:
            self._idMappa[n.id] = n
        self._G.add_nodes_from(self._lista_nodi)
        self._lista_archi = Dao.get_archi(n_bus)
        for id1, id2, peso in self._lista_archi:
            u1 = self._idMappa[id1]
            u2 = self._idMappa[id2]
            self._G.add_edge(u1, u2, weight=peso)

    def get_utenti_conessi(self, nodo):
        utenti = []
        for n in self._G.neighbors(nodo):
            peso = [nodo][n]['weight']
            utenti.append((n,peso))
        utenti.sort(key=lambda x: x[1], reverse =True)
        return utenti
