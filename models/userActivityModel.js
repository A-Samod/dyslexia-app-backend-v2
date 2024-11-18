const mongoose = require("mongoose");

const userActivitySchema = new mongoose.Schema({
  userId: { type: String, required: true },
 // date: { type: Date, default: Date.now },
  date: {
    type: Date,
    default: () => {
      // Set the date in Sri Lankan time (GMT+5:30)
      const now = new Date();
      now.setMinutes(now.getMinutes() + 330); // Offset in minutes for GMT+5:30
      return now;
    },
  },
  usedTime: { type: Number, required: true },
  wrongCount: { type: Number, required: true },
  roundCount: { type: Number, required: true },
  letterOrWord: { type: String, required: true },
  writtenLetterOrWord: { type: String, required: true },
  type: { type: String, required: true, enum: ["single", "two", "three"] },
  correctness: { type: Boolean, required: true },
});

module.exports = mongoose.model("UserActivity", userActivitySchema);
