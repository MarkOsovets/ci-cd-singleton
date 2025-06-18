from singleton import DataBase

def test_singleton_instance():
    db1 = DataBase("root", "1234", 80)
    db2 = DataBase("admin", "pass", 404)
    assert db1 is db2  # оба объекта — один и тот же экземпляр

def test_read_data():
    db = DataBase("root", "1234", 80)
    assert db.read() == "данные"
