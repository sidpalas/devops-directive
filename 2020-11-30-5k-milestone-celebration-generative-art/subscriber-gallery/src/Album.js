import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Link from '@material-ui/core/Link';
import Fuse from 'fuse.js';

const useStyles = makeStyles((theme) => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  heroContent: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(4, 0, 2),
  },
  heroButtons: {
    marginTop: theme.spacing(4),
  },
  cardGrid: {
    paddingTop: theme.spacing(6),
    paddingBottom: theme.spacing(4),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '100%',
  },
  cardContent: {
    flexGrow: 1,
  },
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6),
  }
}));

import artists from './artists.json';
import subscriberData from './subscriber_data_array.json';

const fuse = new Fuse(subscriberData, {
  keys: ['channelId', 'title'],
});

const getRandomElement = (array) => {
  return array[Math.floor(Math.random() * array.length)];
};

const getRandomChannelId = (channelIds) =>
  getRandomElement(channelIds).channelId;

const getRandomImageSrc = (channelIds, artistsIdx) =>
  `${process.env.PUBLIC_URL}/photos/${getRandomChannelId(channelIds)}/${
    artists[artistsIdx]
  }`;

const getMatchingChannelIds = (substring) => {
  if (substring === '') {
    return subscriberData;
  }
  const fuseResult = fuse.search(substring);
  return fuseResult[0] ? [fuseResult[0].item] : subscriberData;
};

const shuffleArray = (array) => {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
};

const getRandomImageSrcs = (substring) => {
  const channelIds = getMatchingChannelIds(substring);
  const emptyArray = shuffleArray([0, 1, 2, 3, 4, 5]);
  return emptyArray.map((i) => getRandomImageSrc(channelIds, i));
};

function SearchResult(props) {
  return props.searchResultStr === '' ? null : (
    <Typography variant="h6" align="center" color="textSecondary" paragraph>
      {props.searchResultStr}
    </Typography>
  );
}

export default function Album() {
  const classes = useStyles();

  const reloadRandom = () => {
    setAlbumData({
      channelId: '',
      searchResultStr: '',
      cards: getRandomImageSrcs(''),
    });
  };

  const reloadSearch = () => {
    const channelIds = getMatchingChannelIds(channelId);
    const searchResultStr =
      channelIds.length === 1
        ? `Channel: ${channelIds[0].title} // ${channelIds[0].channelId}`
        : 'No match found... choosing randomly!';
    setAlbumData({
      channelId: channelId,
      searchResultStr: searchResultStr,
      cards: getRandomImageSrcs(channelId),
    });
  };

  const [albumData, setAlbumData] = useState({
    channelId: '',
    searchResultStr: '',
    cards: getRandomImageSrcs(''),
  });

  const { channelId, searchResultStr, cards } = albumData;
  return (
    <React.Fragment>
      <CssBaseline />
      <main>
        {/* Hero unit */}
        <div className={classes.heroContent}>
          <Container maxWidth="lg">
            <Typography
              component="h1"
              variant="h3"
              align="center"
              color="textPrimary"
              gutterBottom
            >
              DevOps Directive Subscriber Gallery
            </Typography>
            <Typography
              variant="h5"
              align="center"
              color="textSecondary"
              paragraph
            >
              Celebrating 5000 subscribers!!! 🎉🎉🎉
            </Typography>
            <Typography
              variant="body1"
              align="center"
              color="textSecondary"
              paragraph
            >
              (Many channels don't have their subscriptions public. If you want
              me to add your channel, just comment{' '}
              <Link
                href="https://youtu.be/XGcKdsgMrIY"
                target="_blank"
              >
                HERE
              </Link>
              !)
            </Typography>
            <div className={classes.heroButtons}>
              <Grid container spacing={2} justify="center">
                <Grid item>
                  <TextField
                    id="channelId"
                    type="text"
                    inputProps={{}}
                    value={albumData.channelId}
                    onChange={(e) =>
                      setAlbumData({
                        channelId: e.target.value,
                        searchResultStr: searchResultStr,
                        cards: cards,
                      })
                    }
                    onKeyPress={(e) => {
                      if (e.key === 'Enter') {
                        reloadSearch(albumData.channelId);
                      }
                    }}
                  />
                </Grid>
                <Grid item>
                  <Button
                    onClick={reloadSearch}
                    variant="contained"
                    color="primary"
                  >
                    Search By Channel (Name or ID)
                  </Button>
                </Grid>
                <Grid item>
                  <Button
                    onClick={reloadRandom}
                    variant="contained"
                    color="primary"
                  >
                    Reload Random
                  </Button>
                </Grid>
              </Grid>
            </div>
          </Container>
        </div>
        <SearchResult searchResultStr={searchResultStr}></SearchResult>
        <Container className={classes.cardGrid} maxWidth="md">
          {/* End hero unit */}
          <Grid container spacing={4}>
            {cards.map((card, i) => (
              <Grid item key={i} xs={12} sm={6} md={4}>
                <Card className={classes.card}>
                  <CardMedia
                    className={classes.cardMedia}
                    image={card}
                    title={i}
                  />
                </Card>
              </Grid>
            ))}
          </Grid>
        </Container>
        <Typography variant="h6" align="center" color="textSecondary" paragraph>
          (Using the{' '}
          <Link href="https://www.tensorflow.org/tutorials/generative/style_transfer" target="_blank">
            TensorFlow neural style transfer model
          </Link>
          )
        </Typography>
      </main>
    </React.Fragment>
  );
}
