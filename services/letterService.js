const Letter = require('../models/letterModel');

// exports.fetchLettersByType = async (type) => {
//   return await Letter.findOne({ type });
// };

exports.fetchLettersByType = async (type) => {
    const result = await Letter.aggregate([
      { $match: { type } },       // Filter documents by type
      { $sample: { size: 1 } }    // Select one random document
    ]);
  
    return result.length ? result[0] : null; // Return the first result or null if no match
  };

exports.addLetter = async (content, type) => {
  const letter = new Letter({ content, type });
  return await letter.save();
};
