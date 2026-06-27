import { createMDX } from 'fumadocs-mdx/next';

const withMDX = createMDX();

/** @type {import('next').NextConfig} */
const config = {
  reactStrictMode: true,
  output: 'export',
  distDir: 'dist',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/HAPPY-AI' : '',
  basePath: process.env.NODE_ENV === 'production' ? '/HAPPY-AI' : '',
  images: {
    unoptimized: true,
  },
  async redirects() {
    return [
      {
        source: '/docs/advanced/:path*',
        destination: '/docs/deep-learning/:path*',
        permanent: true,
      },
    ];
  },
};

export default withMDX(config);
