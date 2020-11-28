import React from 'react';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Album from './Album.js';
import Box from '@material-ui/core/Box';
import Link from '@material-ui/core/Link';

function Copyright() {
  return (
    <div>
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://devopsdirective.com/">
        DevOps Directive
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography> 
    </div>   
  );
}

export default function App() {
  return (
    <Container maxWidth="lg">
        <Album />
        <Copyright />
    </Container>
  );
}
