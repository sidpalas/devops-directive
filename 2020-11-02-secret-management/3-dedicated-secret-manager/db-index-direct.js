const mongoose = require('mongoose');

// Retrieve password from secret manager
const {SecretManagerServiceClient} = require('@google-cloud/secret-manager');
const name = 'projects/<MY_GCP_PROJECT>/secrets/DB_PASS/versions/latest'
const client = new SecretManagerServiceClient();
const [version] = await client.accessSecretVersion({
  name: name,
});
const DB_PASS = version.payload.data.toString();

const connectionString = `mongodb://myUsername:${DB_PASS}@localhost:27017/myDatabaseName`;

mongoose.connect(connectionString, { useNewUrlParser: true }).catch((e) => {
  console.error('Connection error', e.message);
});

const db = mongoose.connection;

module.exports = db;
