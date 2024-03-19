import './App.scss';
import './Custom.scss';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Fragment } from 'react';

import feeds from './data.json';

import { stripHtml } from "string-strip-html";

function App() {
  return (
    <Container>
      <Row xs={1} md={2}>
      {feeds.map(feed => (
        <Col>
          <FeedTitle title={feed.feedname} />
          <FeedLinks items={feed.items} />
        </Col>
      ))}

      </Row>
    </Container>
  );
}

function FeedTitle({ title }) {
  return <h1 className="display-6 user-select-none">{title}</h1>
}

function FeedLinks({ items }) {
  return items.map(items =>
    <Fragment>
      <Row>
      <a href={items.href} target="_blank"
            className="text-wrap fs-6 lh-1 link-opacity-50-hover feedlink">
               🔗 {items.title}
          </a>
      </Row>
    </Fragment>
    );
}

export default App;
