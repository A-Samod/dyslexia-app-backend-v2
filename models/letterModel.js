const mongoose = require('mongoose');

const letterSchema = new mongoose.Schema({
  content: { type: String, required: true },
  type: { type: String, required: true, enum: ['single', 'two', 'three'] },
});

module.exports = mongoose.model('Letter', letterSchema);
