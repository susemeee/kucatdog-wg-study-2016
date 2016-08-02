# from .memory import TransactableModel
# database = TransactableModel()


class DictModel(dict):
    """
    rollback() 함수가 있는 파이썬 dict입니다.
    rollback 함수는 매 테스트의 종료마다 호출되며,
    상호 테스트간 간섭이 없도록 데이터베이스를 초기화해주는 역할을 합니다.
    """
    def rollback(self):
        self.clear()

database = DictModel()
