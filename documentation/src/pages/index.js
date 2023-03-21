import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import '@trussworks/react-uswds/lib/index.css'
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import { Alert } from '@trussworks/react-uswds'
import { Button } from '@trussworks/react-uswds'

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link to="/docs/intro">
            <Button type="button" primary>
              Getting Started Tutorial - 5min ⏱️
            </Button>            
          </Link>

          <Link to="/docs/api">
            <Button type="button" secondary>
                 API endpoints 🚀
            </Button>
          </Link>
        </div>
      </div>
    </header>
  );
}

let alertText = "This is a beta version of the API. We are still working on the documentation and the API itself. If you have any questions, please contact us at admin@metro.net"

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="API Documentation for Metro's API <head />">

      <HomepageHeader />
        <HomepageFeatures />
    </Layout>
  );
}
