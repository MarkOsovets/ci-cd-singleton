class DataBase:
    __instance = None # будет ссылкой на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение с БД : {self.user}, {self.psw}, {self.port}")

    def close(self):
        print(f"закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('alex', '111333', 404)
print(id(db), id(db2))