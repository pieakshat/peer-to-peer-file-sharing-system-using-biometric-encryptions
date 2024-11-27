import axios from 'axios';

const API_BASE_URL = 'http://localhost:5002/api';

export const generateKeys = async (userInput) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/generate_keys`, { user_input: userInput });
        return response.data; // { public_key, private_key }
    } catch (error) {
        console.error('Error generating keys', error);
    }
};

export const encryptMessage = async (publicPem, message) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/encrypt`, { public_pem: publicPem, message });
        return response.data; // { encrypted_message }
    } catch (error) {
        console.error('Error encrypting message', error);
    }
};

export const decryptMessage = async (privatePem, ciphertext) => {
    try {

        const response = await axios.post(`${API_BASE_URL}/decrypt`, { private_pem: privatePem, ciphertext });
        return response.data; // { decrypted_message }
    } catch (error) {
        console.error('Error decrypting message', error);
    }
};

export const uploadEncrypt = async (formData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/uploadandEncrypt`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data; // { encrypted_cid }
    } catch (error) {
        console.error('Error uploading and encrypting file:', error);
    }
};

export const decryptDownload = async (privatePem, ciphertext) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/decryptDownload`,
            { private_pem: privatePem, ciphertext },
            {
                responseType: "blob", // To handle file download
            });

        return response.data; // The blob data for the downloaded file
    } catch (error) {
        console.error("Error retrieving the file:", error);
        throw error;
    }
}



