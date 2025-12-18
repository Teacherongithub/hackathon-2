import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Chapter 1',
      items: [
        'Chapter-1/introduction',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 2',
      items: [
        'Chapter-2/fundamentals',
        'Chapter-2/workspace',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 3',
      items: [
        'Chapter-3/basic',
        'Chapter-3/xacro',
      ],
    },
    {
      type: 'category',
      label: 'Chapter 4',
      items: [
        'Chapter-4/pid',
        'Chapter-4/teleop',
      ],
    },
  ],
};

export default sidebars;
