// const userActivityService = require('../services/userActivityService');

// exports.submitActivity = async (req, res) => {
//     const { userId, type, text, usedTime, wrongCount, roundCount } = req.body;
//     const activityData = { userId, type, text, usedTime, wrongCount, roundCount };
//     const activity = await userActivityService.saveUserActivity(activityData);
//     res.json({ message: "Activity saved", activity });
// };

// exports.getUserActivity = async (req, res) => {
//     const { userId } = req.params;
//     const activities = await userActivityService.getUserActivity(userId);
//     res.json({ activities });
// };

const userActivityService = require("../services/userActivityService");

exports.getAllActivities = async (req, res) => {
  try {
    const { userId } = req.params;

    if (!userId) {
      return res
        .status(400)
        .json({ success: false, message: "userId is required" });
    }

    const activities = await userActivityService.fetchUserActivities(userId);
    res.json({ success: true, data: activities });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
};

exports.submitActivity = async (req, res) => {
  try {
    const activityData = req.body;
    const activity = await userActivityService.addUserActivity(activityData);
    res.json({ success: true, data: activity });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
};
