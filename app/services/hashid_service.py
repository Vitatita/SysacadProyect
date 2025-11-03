from flask import current_app
from hashids import Hashids


class HashidService:
    def __init__(self, salt: str):
        self.hashids = Hashids(
            salt=current_app.config['HASHIDS_SALT'],
            min_length=current_app.config['HASHIDS_MIN_LENGTH'],
            alphabet=current_app.config['HASHIDS_ALPHABET']
        )

    def encode(self, id: int) -> str:
        return self.hashids.encode(id)

    def decode(self, hashid: str) -> int:
        decoded = self.hashids.decode(hashid)
        return decoded[0] if decoded else None