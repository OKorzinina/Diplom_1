from praktikum.database import Database

class TestDatabase:
    def test_database_initial_counts(self):
        db = Database()
        assert len(db.available_buns()) == 3
        assert len(db.available_ingredients()) == 6

