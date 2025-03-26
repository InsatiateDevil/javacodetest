from fastapi import HTTPException, status


class ObjectNotFound(HTTPException):
    message = "Пользователь не найден"
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self) -> None:
        super().__init__(self.status_code, self.message)


class NotEnoughMoney(HTTPException):
    message = "Для проведения операции недостаточно средств"
    status_code = status.HTTP_409_CONFLICT

    def __init__(self) -> None:
        super().__init__(self.status_code, self.message)
