const dotenv = require("dotenv");

// Load environment variables from .env file
dotenv.config();

module.exports = {
  app: {
    port: process.env.PORT || 6000,
  },
  db: {
    uri: process.env.MONGO_URI || "mongodb://localhost:27017/dyslearn",
  },
};
