# this was the first file not used anywhere anywhere
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import os

def generate_rsa_keypair(fingerprint_hash):   
    # hashing the input from fingerprint 
    input_hash = hashlib.sha256(fingerprint_hash.encode('utf-8')).digest()    

    # using key derivation function 
    # salt = os.urandom(16)
    salt = 567
    salt_bytes = salt.to_bytes((salt.bit_length() + 7) // 8, byteorder='big')
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(), 
        length = 32, 
        salt = salt_bytes, 
        iterations = 100000, 
        backend = default_backend()
    )
    derived_key = kdf.derive(input_hash) # Derive key from user input 

    # using the derived key as a source of randomness to generate the RSA key pair 
    private_key = rsa.generate_private_key(
        public_exponent = 65537, 
        key_size = 2048, 
        backend = default_backend()
    )

    public_key = private_key.public_key()
    return public_key, private_key, salt


def keys_to_pem(public_key, private_key): 
    public_pem = public_key.public_bytes(
        encoding = serialization.Encoding.PEM, 
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

    private_pem = private_key.private_bytes(
        encoding = serialization.Encoding.PEM, 
        format = serialization.PrivateFormat.PKCS8, 
        encryption_algorithm = serialization.NoEncryption()
    ).decode('utf-8')

    return public_pem, private_pem

def load_public_key_from_pem(public_pem): 
    return serialization.load_pem_public_key(
        public_pem.encode('utf-8'), 
        backend=default_backend()
    )

def load_private_key_from_pem(private_pem): 
    return serialization.load_pem_private_key(
        private_pem.encode('utf-8'), 
        password = None, 
        backend = default_backend()
    )


def encrypt_message(public_pem, message): 
    public_key = load_public_key_from_pem(public_pem)

    # encryption
    cipherText = public_key.encrypt(
        message.encode('utf-8'), 
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()), 
            algorithm=hashes.SHA256(), 
            label=None
        )
    )

    # Convert bytes to hex string to make it JSON-serializable
    encrypted_message_hex = cipherText.hex()
    return encrypted_message_hex


# decrypt using private_key (pem format)
def decrypt_message(private_pem, ciphertext): 
    try: 
        print("loading private key from pem")
        private_key = load_private_key_from_pem(private_pem)

    # decrypt the message using private key 
        plaintext = private_key.decrypt(
            ciphertext, 
            padding.OAEP(
                mgf = padding.MGF1(algorithm = hashes.SHA256()), 
                algorithm=hashes.SHA256(), 
                label=None
        )
        )
     
    except Exception as e:  
        print(e)

    return plaintext.decode('utf-8') # converting bytes to string 


# if __name__ == '__main__': 
#     user_input_sender = "sender_fingerprint"
#     user_input_receiver = "receiver_fingerprint"

#     sender_public_key, sender_private_key, sender_salt = generate_rsa_keypair(user_input_sender)
#     receiver_public_key, receiver_private_key, reciever_salt = generate_rsa_keypair(user_input_receiver)

#     receiver_public_pem, receiver_private_pem = keys_to_pem(receiver_public_key, receiver_private_key)
#     print(receiver_public_pem)
#     print("private-pem: ", receiver_private_pem)

#     # Step 2: Sender encrypts a message using the Receiver's public key (in PEM format)
#     message = "This is a secret message for you!"  # Message to encrypt
#     encrypted_message = encrypt_message(receiver_public_pem, message)
#     print(f"Encrypted Message: {encrypted_message}")

#     # Step 3: Receiver decrypts the message using their private key (in PEM format)
#     decrypted_message = decrypt_message(receiver_private_pem, encrypted_message)
#     print(f"Decrypted Message: {decrypted_message}")