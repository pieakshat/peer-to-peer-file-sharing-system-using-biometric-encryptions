import React, { useState } from 'react';
import { decryptMessage } from '../api';
import './styles/DecryptMessage.css';

const DecryptMessage = () => {
    const [privatePem, setPrivatePem] = useState('');
    const [ciphertext, setCiphertext] = useState('');
    const [decryptedMessage, setDecryptedMessage] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleDecrypt = async () => {
        setLoading(true);
        setError('');
        setDecryptedMessage('');
        try {
            const result = await decryptMessage(privatePem, ciphertext);
            setDecryptedMessage(result.decrypted_message);
        } catch (err) {
            console.error('Error decrypting message:', err);
            setError('Failed to decrypt the message. Please check the inputs and try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="decrypt-message-container">
            <h2 className="decrypt-message-title">Decrypt Message</h2>
            <textarea
                className="decrypt-message-textarea"
                placeholder="Enter Private Key (PEM format)"
                value={privatePem}
                onChange={(e) => setPrivatePem(e.target.value)}
                rows={6}
            />
            <textarea
                className="decrypt-message-textarea"
                placeholder="Enter ciphertext (hex-encoded)"
                value={ciphertext}
                onChange={(e) => setCiphertext(e.target.value)}
                rows={4}
            />
            <button
                className="decrypt-message-button"
                onClick={handleDecrypt}
                disabled={loading}
            >
                {loading ? 'Decrypting...' : 'Decrypt'}
            </button>
            {error && <p className="decrypt-message-error">{error}</p>}
            {decryptedMessage && (
                <div className="decrypt-message-output">
                    <h3>Decrypted Message:</h3>
                    <pre>{decryptedMessage}</pre>
                </div>
            )}
        </div>
    );
};

export default DecryptMessage;
