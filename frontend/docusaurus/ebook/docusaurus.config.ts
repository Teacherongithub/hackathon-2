import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  // REQUIRED FIELDS
  title: 'Gemini CLI & ROS 2 Ebook',
  tagline: 'Building the Robotic Nervous System',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-github-username.github.io',
  // Set the /<baseUrl>/ for GitHub pages (usually '/repo-name/')
  baseUrl: '/',

  // GitHub pages deployment config.
  organizationName: 'teacherongithub', 
  projectName: 'ebook', 

  onBrokenLinks: 'throw',
  
  // NEW: Correct place for onBrokenMarkdownLinks in Docusaurus v3+
  markdown: {
    format: 'mdx',
    mermaid: true,
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Note: onBrokenMarkdownLinks was removed from here in v3
        },
        blog: false, // Optional: disables blog if you only want an ebook
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Gemini CLI Ebook',
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Read Ebook',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} Gemini CLI Project.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;