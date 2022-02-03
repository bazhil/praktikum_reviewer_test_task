# TODO: желательно добавить в верх файла указание на кодировку символов: # coding=utf-8
#  Так же желательно добавить вверх описание файла в докстринге на несколько строк:
#  1) что за код содержится в файле?
#  2) кто автор файла?

import datetime as dt


class Record:
    # TODO: отсутствуют докстринги (что делает этот класс? зачем он нужен?) здесь и ниже
    # TODO: какие типы данных у параметров класса? здесь и ниже
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # TODO: конструкция if-else размазана на 3 строчки, лучше сделать по компактнее.
        #  Код поместится в 1 строку и будет лучше читаться
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment

# TODO: если класс Calculator на прямую нигде не используется, лучше сделать его абстрактным
class Calculator:
    # TODO: докстринги и тип данных у переменных?
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        # TODO: отсутствуют докстринги
        # TODO: Какой тип данных у record? добавить обработку невалидного типа
        # TODO: нужна проверка, которая добавляет рекорд, только если он не пустой
        self.records.append(record)

    def get_today_stats(self):
        # TODO: отсутствуют докстринги
        today_stats = 0
        # TODO: переменные начинаются с маленькой буквы
        for Record in self.records:
            # TODO: возможен сценарий, где вместо Record будет None и
            #  попытка получить date от None приведет к ошибке -> учесть
            if Record.date == dt.datetime.now().date():
                # TODO: тут лучше использовать конструкцию +=
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        # TODO: отсутствуют докстринги
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # TODO: условие if плохо читается, лучше сделать более компактным
            # TODO: record должен быть != None (и другим типам/объектам, у которых нет атрибута .date) -> проверять
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # TODO: докстринги и тип данных у переменных?
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # TODO: отсутствуют докстринги
        # TODO: в переменной x точно считаются каллории? -> если это не так, исправить строчку в одном из выводов
        x = self.limit - self.get_today_stats()
        # TODO: возвращаемые строки завести в отдельные переменные и возвращать переменную
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            # TODO: зачем тут скобки и отсутствие пробела перед возвращаемым значением? оформить соответственно PEP8.
            return('Хватит есть!')


class CashCalculator(Calculator):
    # TODO: докстринги и тип данных у переменных?
    # TODO: НА ПОДУМАТЬ: возможно будет лучше офомить эти переменные как атрибуты класса.
    # TODO: убрать float -> int будет достаточно
    # TODO: комментарии у переменных излишни - название переменных говорит само за себя
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # TODO: отсутствуют докстринги +
        #  писать параметры метода в одну строку +
        #  переменные USD_RATE и EURO_RATE уже есть внутри класса, их можно не передавать в метод.
        # TODO: ПРОВЕРИТЬ: переменная currency_type возможно лишняя, чем будет отличаеться от currency?
        # TODO: добавить обработку, на случай, если вместо currency передали невалидное значение
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # TODO: использовать int, а не float
            cash_remained == 1.00
            currency_type = 'руб'
        # TODO: между двумя конструкциями if-else-elif добавить строчку отступа
        if cash_remained > 0:
            # TODO: писать вывод в одну строку
            #  + зачем оборачивать строку в кортеж/скобки?
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            # TODO: завести строку ниже в переменную. Тут возвращать её, а в следующем return переиспользовать её
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # TODO: писать вывод в одну строку
            # TODO: переделать на f-string, чтобы была единая стилистика
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained, #TODO: вместо минуса лучше использовать abs()
                                                     currency_type)

    def get_week_stats(self):
        # TODO: переделать родительский класс в абстрактный и вместо инициализации родителя
        #  звать унаследоваанный метод get_week_stats()
        super().get_week_stats()

# TODO: добавить тесты (под конструкций if __name__ == '__main__':)