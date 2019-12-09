# SWAMI KARUPPASWAMI THUNNAI

import time
import hashlib
import bcrypt
import jwt


class SensibleSecret:
    user_secret = "sensibleSecret7894$#IND"


def hash_password(password):
    sha512 = hashlib.sha512(password.encode("utf8")).hexdigest()
    hashed_password = bcrypt.hashpw(sha512.encode("utf8"), bcrypt.gensalt())
    return hashed_password.decode("utf8")


def verify_password(password, password_hash):
    sha512 = hashlib.sha512(password.encode("utf8")).hexdigest()
    if bcrypt.checkpw(sha512.encode("utf8"), password_hash.encode("utf8")):
        return True
    return False


def generate_token(user_id, password_hash):
    payload = {
        "user_id": user_id,
        "expiry": time.time() + 259200
    }
    encoded_payload = jwt.encode(payload, password_hash+SensibleSecret.user_secret)
    return encoded_payload.decode("utf8")