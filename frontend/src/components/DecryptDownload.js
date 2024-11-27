import React, { useState } from 'react';
import { decryptDownload } from '../api';
import './styles/DecryptDownload.css'; // Import the CSS file

const DecryptDownload = () => {
    const [privatePem, setPrivatePem] = useState('');
    const [ciphertext, setCiphertext] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleDownload = async () => {
        setError('');
        setLoading(true);
        try {
            const response = await decryptDownload(privatePem, ciphertext);
            const blob = new Blob([response], { type: 'application/octet-stream' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'retrieved_file.jpg'; // Default file name
            a.click();
            window.URL.revokeObjectURL(url);
        } catch (err) {
            console.error('Error during download:', err);
            setError('Failed to download the file. Please check your inputs and try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="decrypt-download-container">
            <h2 className="decrypt-download-title">Decrypt & Download File</h2>
            <textarea
                className="decrypt-download-textarea"
                placeholder="Enter ciphertext"
                value={ciphertext}
                onChange={(e) => setCiphertext(e.target.value)}
                rows={4}
            />
            <button
                className="decrypt-download-button"
                onClick={handleDownload}
                disabled={loading}
            >
                {loading ? 'Downloading...' : 'Decrypt & Download'}
            </button>
            {error && <p className="decrypt-download-error">{error}</p>}
        </div>
    );
};

export default DecryptDownload;
