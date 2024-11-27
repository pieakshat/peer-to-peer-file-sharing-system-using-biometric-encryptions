import React, { useState } from 'react';
import { generateKeys } from '../api';
import './styles/GenerateKeys.css';

function GenerateKeys() {
    const [userInput, setUserInput] = useState('kjkszpj');
    const [publicKey, setPublicKey] = useState('');
    const [privateKey, setPrivateKey] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleGenerateKeys = async () => {
        setErrorMessage(''); // Clear any previous error messages
        const keys = await generateKeys(userInput);
        if (keys && keys.public_key && keys.private_key) {
            setPublicKey(keys.public_key);
            setPrivateKey(keys.private_key);
        } else {
            setErrorMessage('Failed to generate keys. Please try again.');
        }
    };

    return (
        <div className="generate-keys-container">
            <h2 className="generate-keys-title">Generate Keys</h2>
            <button className="generate-keys-button" onClick={handleGenerateKeys}>
                Generate Keys
            </button>
            {errorMessage && <p className="generate-keys-error">{errorMessage}</p>}
            <div className="generate-keys-output">
                <h3 className="generate-keys-output-title">Public Key</h3>
                <textarea
                    className="generate-keys-textarea"
                    value={publicKey}
                    readOnly
                />
                <h3 className="generate-keys-output-title">Private Key</h3>
                <textarea
                    className="generate-keys-textarea"
                    value={privateKey}
                    readOnly
                />
            </div>
        </div>
    );
}

export default GenerateKeys;
