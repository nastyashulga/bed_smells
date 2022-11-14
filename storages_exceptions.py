# all errors' description
class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    message = 'В выбранном пункте недостаточно места'


class UnknownItemError(BaseError):
    message = 'В выбранном пункте отсутствует данный товар'


class NotEnoughItemError(BaseError):
    message = 'В выбранном пункте недостаточно товара'


class MoreThanFiveUniquesError(BaseError):
    message = 'В выбранном пункте 5 или более уникальных товаров'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'Неизвестный пункт'



