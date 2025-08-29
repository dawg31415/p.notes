import gnupg
import os
from constants.consts import GPGEXT

gpg = gnupg.GPG(gnupghome='/home/dawggg/.gnupg')

def encrypt(filepath: str, passphrase: str, clean: bool = True) -> None:
    with open(filepath, "rb") as f:
        encrypted = gpg.encrypt_file(
            f,
            recipients=None,
            passphrase=passphrase,
            symmetric='AES256',
            output=f"{filepath}.gpg"
        )
    if clean:
        os.remove(filepath)

def decrypt(filepath: str, passphrase: str) -> str:
    with open(filepath, "rb") as f:
        decrypted = gpg.decrypt_file(f, passphrase=passphrase)
        return decrypted.ok, decrypted.data.decode("utf-8")
