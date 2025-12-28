import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

const Home: React.FC = () => {
  return (
    <Layout title="My Ebook RAG Chatbot" description="Home page of your RAG Chatbot project">
      <div style={{ textAlign: 'center', margin: '4rem 0' }}>
        <h1>Welcome to My Ebook RAG Chatbot</h1>
        <p>Interact with your ebook using our AI-powered chatbot.</p>

        <div style={{ marginTop: '2rem' }}>
          <Link
            to="/chat"
            style={{
              padding: '1rem 2rem',
              backgroundColor: '#007bff',
              color: '#fff',
              borderRadius: '8px',
              textDecoration: 'none',
              fontWeight: 'bold',
            }}
          >
            Go to Chatbot
          </Link>
        </div>

        <div style={{ marginTop: '4rem', color: '#555' }}>
          <p>Make sure your backend is running at <code>http://127.0.0.1:8001</code> for the chatbot to work.</p>
        </div>
      </div>
    </Layout>
  );
};

export default Home;
