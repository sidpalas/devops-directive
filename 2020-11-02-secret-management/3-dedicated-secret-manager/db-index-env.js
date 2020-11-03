const dotenv = require('../3-dedicated-secret-manager/node_modules/dotenv')
const mongoose = require('mongoose');

const connectionString = `mongodb://myUsername:${process.env.DB_PASS}@localhost:27017/myDatabaseName`;

mongoose.connect(connectionString, { useNewUrlParser: true }).catch((e) => {
  console.error('Connection error', e.message);
});

const db = mongoose.connection;

module.exports = db;
