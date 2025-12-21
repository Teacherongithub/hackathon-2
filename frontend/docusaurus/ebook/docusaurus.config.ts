import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

<<<<<<< HEAD
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
=======
// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'My Site',
  tagline: 'Dinosaurs are cool',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
<<<<<<< HEAD
          // Note: onBrokenMarkdownLinks was removed from here in v3
        },
        blog: false, // Optional: disables blog if you only want an ebook
=======
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
<<<<<<< HEAD
    navbar: {
      title: 'Gemini CLI Ebook',
=======
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
<<<<<<< HEAD
          label: 'Read Ebook',
=======
          label: 'Tutorial',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
        },
      ],
    },
    footer: {
      style: 'dark',
<<<<<<< HEAD
      copyright: `Copyright © ${new Date().getFullYear()} Gemini CLI Project.`,
=======
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'X',
              href: 'https://x.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/facebook/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

<<<<<<< HEAD
export default config;
=======
export default config;
>>>>>>> 646602f5 (Finilized structure: unified backend and frontend/ebook)
