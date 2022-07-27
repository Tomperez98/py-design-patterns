from patterns import singleton


def test_pattern():
    instance_1 = singleton.DatabaseManager(database_url="url")
    instance_2 = singleton.DatabaseManager(database_url="url")

    id_1 = id(instance_1)
    id_2 = id(instance_2)
    assert id_1 == id_2


def test_connection():
    db_manager = singleton.DatabaseManager(database_url="url")
    assert db_manager.connect() == "Conecting to database..."
