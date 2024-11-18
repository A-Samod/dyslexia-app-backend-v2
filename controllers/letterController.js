const letterService = require("../services/letterService");

exports.getLettersByType = async (req, res) => {
  try {
    const { type } = req.params;
    const letters = await letterService.fetchLettersByType(type);
    res.json({ success: true, data: letters });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
};

exports.addLetter = async (req, res) => {
  try {
    const { content, type } = req.body;
    const letter = await letterService.addLetter(content, type);
    res.json({ success: true, data: letter });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
};
