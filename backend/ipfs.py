import requests
from rsa import generate_rsa_keypair, keys_to_pem, encrypt_message, decrypt_message
import mimetypes

def add_file_to_ipfs(file, public_pem):
    
    files = {'file': (file.filename, file)}
    print(public_pem)
    
    response = requests.post('http://127.0.0.1:5001/api/v0/add', files=files)       # ipfs dameon server api
    
    if response.status_code != 200:
        raise Exception(f"Failed to add file to IPFS. Status code: {response.status_code}, Response: {response.text}")
    
    res_json = response.json()
    print(f"File added to IPFS with hash: {res_json['Hash']}")
    cid = res_json['Hash']

    print("sending cid for encryption")
    encrypted_cid = encrypt_message(public_pem, cid)
    print("got encrypted cid")
    return encrypted_cid

import io

def get_file_from_ipfs(encrypted_cid, private_pem): 
    print("Starting decryption process")
    
    # Decrypt the CID
    cid = decrypt_message(private_pem, encrypted_cid)
    print("Decrypted CID:", cid)
    
    try: 
        # Fetch the file from IPFS
        response = requests.post(f'http://127.0.0.1:5001/api/v0/cat?arg={cid}')     
        if response.status_code == 200: 
            print("File retrieved from IPFS")
            
            # Write file temporarily to infer MIME type
            output_path = './files/retrieved.jpg'
            with open(output_path, 'wb') as output_file:
                output_file.write(response.content)
            
            # Infer MIME type
            mime_type, _ = mimetypes.guess_type(output_path)
            mime_type = mime_type or "application/octet-stream"  # Fallback to binary

            # Return the file content and MIME type
            return io.BytesIO(response.content), mime_type
        else:
            print(f"Error fetching file: {response.status_code} - {response.text}")
            raise Exception(f"Failed to fetch file: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error downloading the file: {str(e)}")
        raise




