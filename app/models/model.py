import hashlib


class Model:
    def __init__(self, display_name: str, display_fields: list):
        self.database = dict()
        self.display_name = display_name
        self.display_fields = display_fields

    def add(self, data: dict):
        if data:
            # calculate a hash for the data
            hash_str = ''
            for field in self.display_fields:
                hash_str += data.get(field)
            data_hash = hashlib.sha256(hash_str.encode('utf-8')).hexdigest()

            # check if that hash already exists in database, if not then add
            if data_hash not in self.database:
                self.database.setdefault(data_hash, data)

    @staticmethod
    def save():
        pass

    def query_all(self) -> list:
        return list(self.database.values())
