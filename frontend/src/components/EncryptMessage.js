import React, { useState } from 'react';
import { encryptMessage } from '../api';
import './styles/EncryptMessage.css';

function EncryptMessage() {
    const [publicPem, setPublicPem] = useState('');
    const [message, setMessage] = useState('');
    const [encryptedMessage, setEncryptedMessage] = useState('');

    const handleEncryptMessage = async () => {
        const response = await encryptMessage(publicPem, message);
        setEncryptedMessage(response.encrypted_message);
    };

    return (
        <div className="encrypt-message-container">
            <h2 className="encrypt-message-title">Encrypt Message</h2>
            <textarea
                className="encrypt-message-textarea"
                placeholder="Enter public key"
                value={publicPem}
                onChange={(e) => setPublicPem(e.target.value)}
                required
            />
            <input
                className="encrypt-message-input"
                type="text"
                placeholder="Enter message to encrypt"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                required
            />
            <button
                className="encrypt-message-button"
                onClick={handleEncryptMessage}
            >
                Encrypt
            </button>
            <div className="encrypt-message-output">
                <h3 className="encrypt-message-output-title">Encrypted Message</h3>
                <textarea
                    className="encrypt-message-output-textarea"
                    value={encryptedMessage}
                    readOnly
                />
            </div>
        </div>
    );
}

export default EncryptMessage;
