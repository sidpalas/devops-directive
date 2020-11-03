const dotenv = require('dotenv')
const mongoose = require('mongoose');

dotenv.config({ path: './secrets.env' })

const connectionString = 
  `mongodb://myUser:${process.env.DB_PASS}@localhost:27017/myDatabaseName`;

mongoose.connect(connectionString, { useNewUrlParser: true }).catch((e) => {
  console.error('Connection error', e.message);
});

const db = mongoose.connection;

module.exports = db;
