import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import GenerateKeys from './components/GenerateKeys';
import EncryptMessage from './components/EncryptMessage';
import DecryptMessage from './components/DecryptMessage';
import UploadEncrypt from './components/UploadEncrypt';
import DecryptDownload from './components/DecryptDownload';
import './App.css'; // Import the custom CSS

const App = () => {
  return (
    <Router>
      <div>
        <nav className="navbar">
          <div className="nav-brand">
            <Link to="/" className="nav-title">BioCrypt</Link>
          </div>
          <ul className="nav-links">
            <li><Link to="/generate-keys" className="nav-link">Generate Keys</Link></li>
            <li><Link to="/encrypt-message" className="nav-link">Encrypt Message</Link></li>
            <li><Link to="/decrypt-message" className="nav-link">Decrypt Message</Link></li>
            <li><Link to="/upload-encrypt" className="nav-link">Upload & Encrypt</Link></li>
            <li><Link to="/decrypt-download" className="nav-link">Decrypt & Download</Link></li>
          </ul>
        </nav>

        <div className="content">
          <Routes>
            <Route path="/generate-keys" element={<GenerateKeys />} />
            <Route path="/encrypt-message" element={<EncryptMessage />} />
            <Route path="/decrypt-message" element={<DecryptMessage />} />
            <Route path="/upload-encrypt" element={<UploadEncrypt />} />
            <Route path="/decrypt-download" element={<DecryptDownload />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
