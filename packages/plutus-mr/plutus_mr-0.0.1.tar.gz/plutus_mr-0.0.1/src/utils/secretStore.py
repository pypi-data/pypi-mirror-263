# Usage:

# To store a secret :
# Input: A dictionary containing the key, value pairs of the secrets
# secret_store = SecretStore()
# secret_store.add_secret({"Secret Name": "Secret"})

# To retrieve secrets:
# secret_store = SecretStore()

# Retrieve all the secrets stored
# decrypted_text = json.loads(secret_store.decrypt())

# Retrieve specific secrets stored -> Pass keys as list
# even when retrieving a single key
# decrypted_text = json.loads(secret_store.decrypt(["Key1","Key2"]))

import json
import os.path
from io import BytesIO
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pydantic import BaseModel
import config.constants as ct


class SecretStore(BaseModel):
    path: str = ct.crypt_path
    text: dict = {}
    config: dict = {"cipher_text": None, "key": None, "tag": None, "nonce": None}

    def add_secret(self, secret: dict):

        if os.path.isfile(self.path + "key.bin"):
            print("Secret Store Already Exists")
            secret_container, mac_input = self.decrypt(update=True)
            updated_container = secret_container | secret
            self.encrypt(updated_container, mac_input)
            print("Done")
        else:
            self.encrypt(secret)
            print("Done")

    # AES encryption with GCM mode

    def encrypt(self, secret: dict, mac_input=None):

        if mac_input is None:
            mac_input = str.encode(input("Enter MAC: "))
        elif mac_input is not None:
            mac_input = mac_input
        self.config["key"] = get_random_bytes(16)

        cipher = AES.new(self.config["key"], AES.MODE_GCM)
        cipher.update(mac_input)

        text_bytes = json.dumps(secret, indent=4, separators=(',', ': ')).encode('utf-8')
        self.config["cipher_text"], self.config["tag"] = cipher.encrypt_and_digest(text_bytes)
        self.config["nonce"] = cipher.nonce

        for i in self.config:
            with open(self.path + i + ".bin", "wb+") as f:
                # noinspection PyTypeChecke
                f.write(BytesIO(self.config[i]).getbuffer())


    def decrypt(self, update: bool = False, secret_keys: list = None):

        mac_input = str.encode(input("Enter MAC: "))
        for i in self.config:
            in_file = open(self.path + i + ".bin", "rb")
            self.config[i] = in_file.read()
            in_file.close()

        decrypt_cipher = AES.new(self.config["key"], AES.MODE_GCM, nonce=self.config["nonce"])
        decrypt_cipher.update(mac_input)
        plain_text = decrypt_cipher.decrypt_and_verify(self.config["cipher_text"], self.config["tag"])
        decoded = json.loads(plain_text.decode("utf-8"))
        if secret_keys is not None:
            query_keys = set(secret_keys)
            store_keys = decoded.keys()
            if query_keys.issubset(store_keys):  # All the query keys are present
                print("All keys are present")
                decoded = dict((k, decoded[k]) for k in query_keys)
                return decoded
            elif query_keys.isdisjoint(store_keys):  # None of the query keys are present
                print("None of the keys are present")
                return None
            else:  # Few of the query keys are present
                keys_present = query_keys.intersection(store_keys)
                keys_not_present = query_keys.difference(store_keys)
                print("Following keys are not present: ", keys_not_present)
                decoded = dict((k, decoded[k]) for k in keys_present)
                return decoded
        if not update:
            return decoded
        if update:
            return decoded, mac_input
