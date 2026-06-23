from model.model import Model
from UI.view import View
import flet as ft

class Controller:
    def __init__(self, view : View, model : Model):
        self._view = view
        self._model = model

    def handler_crea_grafo(self, e):
        try:
            n_bus = int(self._view._txt_nBus.value)
        except ValueError:
            self._view.show_alert(f"Valore inserito non valido")
            return

        if n_bus < 0:
            self._view.show_alert(f"Valore inserito non valido, dev'essere maggiore di 0")
            return

        self._model.build_graph(n_bus)
        self._view._lst_result.controls.clear()
        self._view._lst_result.controls.append(ft.Text(f"Grafo creato correttamente. Nodi: {self._model._G.number_of_nodes()} - Archi: {self._model._G.number_of_edges()}"))
        self._view.update_page()

    def handler_utenti_connessi(self, e):
        self._view._lst_result.controls.clear()

        for n, w in self._model.get_utenti_conessi(self._model._idMappa[nodo]):
            self._view._lst_result.controls.append(ft.Text(f"Connessi: {n} - strenght {w}"))

        self._view.update_page()

