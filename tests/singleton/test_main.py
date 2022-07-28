import pytest

from patterns import singleton


def test_pattern():
    db_manager = singleton.DatabaseManager(database_url="url")
    with pytest.raises(Exception) as exc:
        singleton.DatabaseManager(database_url="url")
        assert (
            str(exc.value)
            == "This class is a singleton. Use the already created instance "
            "or delete it before instanciating a new one"
        )

    assert db_manager.connect() == "Conecting to database..."
