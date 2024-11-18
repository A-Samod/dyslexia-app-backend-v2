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
