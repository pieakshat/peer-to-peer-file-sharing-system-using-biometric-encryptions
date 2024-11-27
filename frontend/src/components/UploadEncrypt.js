import React, { useState } from 'react';
import { uploadEncrypt } from '../api';
import './styles/UploadEncrypt.css';

function UploadEncrypt() {
    const [publicKey, setPublicKey] = useState('');
    const [file, setFile] = useState(null);
    const [encryptedCid, setEncryptedCid] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handlePublicKeyChange = (e) => {
        setPublicKey(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!file || !publicKey) {
            alert('Please provide both a file and a public key.');
            return;
        }

        // Create FormData object to send the file and public key
        const formData = new FormData();
        formData.append('file', file);
        formData.append('public_pem', publicKey);

        try {
            const response = await uploadEncrypt(formData);
            if (response && response.encrypted_cid) {
                setEncryptedCid(response.encrypted_cid);
            } else {
                alert('Failed to upload and encrypt the file. Please try again.');
            }
        } catch (error) {
            console.error('Error uploading and encrypting the file:', error);
        }
    };

    return (
        <div className="upload-encrypt-container">
            <h2 className="upload-encrypt-title">Send file</h2>
            <form className="upload-encrypt-form" onSubmit={handleSubmit}>
                <div className="upload-encrypt-field">
                    <label className="upload-encrypt-label">Receiver's Public Key:</label>
                    <textarea
                        className="upload-encrypt-textarea"
                        value={publicKey}
                        onChange={handlePublicKeyChange}
                        placeholder="Enter public key"
                    />
                </div>
                <div className="upload-encrypt-field">
                    <label className="upload-encrypt-label">Upload File:</label>
                    <input
                        className="upload-encrypt-input"
                        type="file"
                        onChange={handleFileChange}
                    />
                </div>
                <button className="upload-encrypt-button" type="submit">
                    Upload and Encrypt
                </button>
            </form>
            {encryptedCid && (
                <div className="upload-encrypt-output">
                    <h3 className="upload-encrypt-output-title">Encrypted CID:</h3>
                    <textarea
                        className="upload-encrypt-output-textarea"
                        readOnly
                        value={encryptedCid}
                    />
                </div>
            )}
        </div>
    );
}

export default UploadEncrypt;
