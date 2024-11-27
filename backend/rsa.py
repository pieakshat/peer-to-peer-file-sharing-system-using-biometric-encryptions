from Crypto.PublicKey import RSA
import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import PKCS1_OAEP

# Custom Deterministic Random Generator
class DeterministicRandomGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.hasher = hashlib.sha256(seed)
        self.buffer = b''

    def __call__(self, n):
        while len(self.buffer) < n:
            self.hasher.update(self.seed)
            self.buffer += self.hasher.digest()
        result = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return result

def generate_rsa_keypair(fingerprint_hash):   
    # Hash the input from fingerprint 
    print("starting...")
    input_hash = hashlib.sha256(fingerprint_hash.encode('utf-8')).digest()    

    # Using key derivation function 
    salt = b'some constant salt'  # Use a constant salt for determinism
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(), 
        length = 32, 
        salt = salt, 
        iterations = 100000, 
        backend = default_backend()
    )
    derived_key = kdf.derive(input_hash)  # Derive key from user input 

    # Use derived_key as seed for deterministic RNG
    deterministic_random_generator = DeterministicRandomGenerator(derived_key)

    # Generate RSA key pair using deterministic RNG
    key = RSA.generate(2048, randfunc=deterministic_random_generator)
    public_key = key.publickey()
    return public_key, key

def keys_to_pem(public_key, private_key): 
    public_pem = public_key.export_key(format='PEM').decode('utf-8')
    private_pem = private_key.export_key(format='PEM').decode('utf-8')
    return public_pem, private_pem

def load_public_key_from_pem(public_pem): 
    return RSA.import_key(public_pem.encode('utf-8'))

def load_private_key_from_pem(private_pem): 
    return RSA.import_key(private_pem.encode('utf-8'))

def encrypt_message(public_pem, message): 
    public_key = load_public_key_from_pem(public_pem)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    encrypted_message_hex = ciphertext.hex()
    return encrypted_message_hex

def decrypt_message(private_pem, encrypted_message_hex):
    try:  
        private_key = load_private_key_from_pem(private_pem)
        ciphertext = bytes.fromhex(encrypted_message_hex)
        cipher = PKCS1_OAEP.new(private_key)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode('utf-8')
    except Exception as e: 
        print(e)

def test_deterministic_key_generation():
    # Input to generate the key pair
    fingerprint_hash = "test_fingerprint"

    # Generate key pair twice with the same input
    public_key1, private_key1 = generate_rsa_keypair(fingerprint_hash)
    public_key2, private_key2 = generate_rsa_keypair(fingerprint_hash)

    # Convert keys to PEM format
    public_pem1, private_pem1 = keys_to_pem(public_key1, private_key1)
    public_pem2, private_pem2 = keys_to_pem(public_key2, private_key2)

    # Compare the PEM strings
    assert public_pem1 == public_pem2, "Public keys do not match!"
    assert private_pem1 == private_pem2, "Private keys do not match!"

    print("Test passed: Key pairs generated from the same input are identical.")

if __name__ == '__main__': 
    # Run the test
    test_deterministic_key_generation()

    # Proceed with the rest of the code
    user_input_sender = "sender_fingerprint"
    user_input_receiver = "receiver_fingerprint"

    sender_public_key, sender_private_key = generate_rsa_keypair(user_input_sender)
    receiver_public_key, receiver_private_key = generate_rsa_keypair(user_input_receiver)

    receiver_public_pem, receiver_private_pem = keys_to_pem(receiver_public_key, receiver_private_key)
    print("Receiver Public Key PEM:\n", receiver_public_pem)
    print("Receiver Private Key PEM:\n", receiver_private_pem)

    # Sender encrypts a message using the Receiver's public key (in PEM format)
    message = "This is a secret message for you!"  # Message to encrypt
    encrypted_message = encrypt_message(receiver_public_pem, message)
    print(f"Encrypted Message: {encrypted_message}")

    # Receiver decrypts the message using their private key (in PEM format)
    decrypted_message = decrypt_message(receiver_private_pem, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
