import React, { useState } from 'react';
import Layout from '@theme/Layout';
import './chat.css'; // Optional: create a CSS file for styling

const Chatbot: React.FC = () => {
  const [query, setQuery] = useState('');
  const [chatHistory, setChatHistory] = useState<{ sender: string; message: string }[]>([]);
  const [loading, setLoading] = useState(false);

  // Function to call the /chat API
  const handleChat = async () => {
    if (!query.trim()) return;

    setChatHistory([...chatHistory, { sender: 'User', message: query }]);
    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8001/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });
      const data = await response.json();
      setChatHistory(prev => [...prev, { sender: 'Bot', message: data.answer || 'No answer' }]);
      setQuery('');
    } catch (error) {
      console.error(error);
      setChatHistory(prev => [...prev, { sender: 'Bot', message: 'Error connecting to backend.' }]);
    } finally {
      setLoading(false);
    }
  };

  // Optional: trigger ingestion (call /ingest once)
  const handleIngest = async () => {
    try {
      await fetch('http://127.0.0.1:8001/ingest', { method: 'POST' });
      alert('Documents ingested successfully!');
    } catch (error) {
      console.error(error);
      alert('Failed to ingest documents.');
    }
  };

  return (
    <Layout title="RAG Chatbot" description="Ask questions about your ebook">
      <div style={{ maxWidth: '700px', margin: '0 auto', padding: '2rem' }}>
        <h1>RAG Chatbot</h1>
        <button onClick={handleIngest} style={{ marginBottom: '1rem' }}>Ingest Documents</button>

        <div className="chat-window" style={{ border: '1px solid #ccc', padding: '1rem', minHeight: '300px', marginBottom: '1rem', overflowY: 'auto' }}>
          {chatHistory.map((msg, idx) => (
            <div key={idx} style={{ margin: '0.5rem 0', textAlign: msg.sender === 'User' ? 'right' : 'left' }}>
              <strong>{msg.sender}:</strong> {msg.message}
            </div>
          ))}
          {loading && <div>Bot is typing...</div>}
        </div>

        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <input
            type="text"
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="Ask something..."
            style={{ flex: 1, padding: '0.5rem' }}
            onKeyDown={e => { if (e.key === 'Enter') handleChat(); }}
          />
          <button onClick={handleChat} style={{ padding: '0.5rem 1rem' }}>Send</button>
        </div>
      </div>
    </Layout>
  );
};

export default Chatbot;
