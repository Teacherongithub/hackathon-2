<<<<<<< HEAD
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
=======
import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Docusaurus Tutorial - 5min ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
