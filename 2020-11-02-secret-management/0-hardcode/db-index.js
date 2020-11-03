const mongoose = require('mongoose');

const connectionString = 
  'mongodb://myUser:superSecretPassword@localhost:27017/databaseName';

mongoose.connect(connectionString, { useNewUrlParser: true }).catch((e) => {
  console.error('Connection error', e.message);
});

const db = mongoose.connection;

module.exports = db;
