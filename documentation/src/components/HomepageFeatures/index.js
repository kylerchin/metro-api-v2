import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import { Card,CardBody,CardFooter,CardGroup,CardHeader,CardMedia } from '@trussworks/react-uswds'
const FeatureList = [
  {
    title: 'Static + Realtime GTFS',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Access LA Metro&apos;s static and realtime GTFS data as JSON via our API endpoints.
      </>
    ),
  },
  {
    title: 'Powered by Metro\'s API',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Add Metro's API to your website or app and let us know!
      </>
    ),
  },
  {
    title: 'Constant Development',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        We're constantly working on our API as we get it to a stable release!
      </>
    ),
  },
];

function CardFeature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <Card>
        <CardHeader className="bg-base-lightest">
          <h3 className="usa-card__heading">{title}</h3>
        </CardHeader>
        <CardMedia imageClass="add-aspect-16x9">
          <Svg className={styles.featureSVG} 
            alt="An image's description"
          />
        </CardMedia>
        <CardBody className="padding-top-3">
          <p>{description}</p>
        </CardBody>
      </Card>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <div className={styles.features}>
      <div className="container">
        <CardGroup>
          {FeatureList.map((props, idx) => (
            <CardFeature key={idx} {...props} />
          ))}
          </CardGroup>
      </div>
    </div>
  );
}
