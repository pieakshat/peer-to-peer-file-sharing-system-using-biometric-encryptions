To start this project: 

1. git clone

3. go to the backend folder and run:\n 
 ```python3 app.py```\n
ensure that you have all the python librarise installed
this will start the server on port 5002

5. open another terminal window and run the ipfs node:
   ```ipfs daemon```
  ensure that you get this message after starting the ipfs node
```RPC API server listening on /ip4/127.0.0.1/tcp/5001```
   
7. go to the frontend folder and run:
   ```npm install```
   ```npm start```
   

The idea of this project is simple. 

   we use RSA algorithms to generate keypairs from the fingerprint hash. the keypairs generated are deterministic.

   when Bob wants to share a file to Alice. first uploads the file to IPFS and a CID is returned.
   Bob also has to know the public key of Alice to share the file with her. 
   the CID is now encrypted using Alice's public key.
   Now bob can send the encrypted CID to Alice
   Alice will be able to decrypt the shared encrypted CID and retrive the file from the IPFS network  


   [learn more about this project](https://docs.google.com/document/d/1qeNrZZ94fpos4fDs44NGCM_LcWzZRsbUXjIduBIDrgY/edit?usp=sharing)

   
