from classes import Shop, Store, Request
from storages_exceptions import BaseError


# main func
def main():
    shop_1 = Shop(items={'картошка': 1, 'морковка': 2, 'лук': 3, 'помидор': 3, 'огурец': 2})
    store_1 = Store(items={'диск': 1, 'кассета': 2, 'дискета': 3})
    departments = {'магазин': shop_1, 'склад': store_1}
    while True:

        for item in departments:
            print(f'В {item} хранится {departments[item].get_items()}')

        user_input = input('Доставить n товара из пункта А в пункт Б\nВведите "стоп" чтобы закончить\n').lower().strip()

        if user_input == 'стоп':
            break

        try:
            user_req = Request(user_input, departments)

            destination = departments[user_req.destination]
            departure = departments[user_req.departure]

            departure.remove(user_req.product, user_req.amount, departure)
            destination.add(user_req.product, user_req.amount)

            print(f'Курьер забрал {user_req.amount} {user_req.product} со {departure}')
            print(f'Курьер везет {user_req.amount} {user_req.product} в {destination}')
            print(f'Курьер доставил {user_req.amount} {user_req.product} в {destination}')
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
