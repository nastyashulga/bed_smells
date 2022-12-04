# create a Request class
class Request:
    def __init__(self, user_string, list_of_shops):
        request_split = user_string.split(' ')

        self.amount = int(request_split[1])
        self.product = request_split[2]
        self.departure = request_split[4]
        self.destination = request_split[6]

        if self.destination not in list_of_shops or self.departure not in list_of_shops:
            raise UnknownStorageError