# from .memory import TransactableModel
# database = TransactableModel()


class DictModel(dict):
    def rollback(self):
        self.clear()

database = DictModel()
