const Letter = require('../models/letterModel');
let lastFetchedLetterId = null; 


exports.fetchLettersByType = async (type) => {
  const query = { type };

  // Exclude the last fetched letter
  if (lastFetchedLetterId) {
    query._id = { $ne: lastFetchedLetterId };
  }

  const result = await Letter.aggregate([
    { $match: query },        // Filter documents by type and exclude last fetched
    { $sample: { size: 1 } }  // Select one random document
  ]);

  if (result.length) {
    lastFetchedLetterId = result[0]._id; // Update the last fetched letter ID
    return result[0];                    // Return the fetched document
  }

  return null; // Return null if no match
};

exports.addLetter = async (content, type) => {
  const letter = new Letter({ content, type });
  return await letter.save();
};
