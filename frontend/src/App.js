import './App.scss';
import './Custom.scss';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Fragment } from 'react';

// import feeds from './data.json';
const feeds = await fetch("https://raw.githubusercontent.com/Nexact/watchtower/main/data.json").then(r => r.json())

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
  return items.slice(0,10).map(items =>
    <Fragment>
      <Row className='p-1'>
      <a href={items.href} target="_blank"
            className="text-wrap fs-6 lh-1 link-opacity-50-hover feedlink" rel="noreferrer">
               🔗 {items.title}
          </a>
      </Row>
    </Fragment>
    );
}

export default App;
