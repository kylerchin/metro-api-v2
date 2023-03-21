import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import { Card,CardBody,CardFooter,CardGroup,CardHeader,CardMedia } from '@trussworks/react-uswds'
const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Docusaurus was designed from the ground up to be easily installed and
        used to get your website up and running quickly.
      </>
    ),
  },
  {
    title: 'Focus on What Matters',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Docusaurus lets you focus on your docs, and we&apos;ll do the chores. Go
        ahead and move your docs into the <code>docs</code> directory.
      </>
    ),
  },
  {
    title: 'Powered by React',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Extend or customize your website layout by reusing React. Docusaurus can
        be extended while reusing the same header and footer.
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
