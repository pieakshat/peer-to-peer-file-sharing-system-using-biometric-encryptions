import time
import hashlib
import subprocess 

def wait_for_touch_id():
    try:
    
        print("starting swift program")
        result = subprocess.run(
            ["swift", "id.swift"],
            capture_output=True,
            text=True
        )
        print("Swift program done: ", result)
        if result.returncode == 0:
            print("Touch ID authentication successful!")
            return True
        else:
            print("Touch ID authentication failed!")
            print("Error:", result.stderr.strip())
            return False
    except Exception as e:
        print("An error occurred:", str(e))
        return False

def fingerprint_scan():
    return wait_for_touch_id()
    # print("Scanning...")
    # time.sleep(2)  
    
    # Get user input to simulate fingerprint data
    # user_input = input("Enter your fingerprint ID (or any random string): ")
    # return user_input

# def generate_rsa_keypair(user_input):
#     # Hash the simulated fingerprint data
#     input_hash = hashlib.sha256(user_input.encode('utf-8')).digest()
    
#     print("\nGenerated hash from fingerprint:")
#     print(input_hash.hex())  # Display the hash for verification
    
#     # Generate RSA key pair (remaining functionality as your original code)
#     # This part is retained from your provided script for context
#     from cryptography.hazmat.primitives.asymmetric import rsa
#     from cryptography.hazmat.primitives import serialization
#     private_key = rsa.generate_private_key(
#         public_exponent=65537,
#         key_size=2048,
#     )
#     public_key = private_key.public_key()
    
#     public_pem = public_key.public_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PublicFormat.SubjectPublicKeyInfo
#     )
#     private_pem = private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.PKCS8,
#         encryption_algorithm=serialization.NoEncryption()
#     )
    
#     print("\nPublic Key PEM:")
#     print(public_pem.decode('utf-8'))
#     print("\nPrivate Key PEM:")
#     print(private_pem.decode('utf-8'))

# Simulate fingerprint scanning and key generation
# user_fingerprint = fingerprint_scan()
# generate_rsa_keypair(user_fingerprint)
