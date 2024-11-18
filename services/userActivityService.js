const UserActivity = require('../models/userActivityModel');
const firestore = require('../config/firebaseConfig');

exports.fetchUserActivities = async (userId) => {
  const activities = await UserActivity.find({ userId }, null, { sort: { date: -1 } });

  // Convert usedTime from seconds to minutes:seconds format
  const formattedActivities = activities.map((activity) => {
    const minutes = Math.floor(activity.usedTime / 60);
    const seconds = activity.usedTime % 60;
    const formattedUsedTime = `${minutes}:${seconds.toString().padStart(2, '0')}`; // Format as MM:SS

    return {
      ...activity.toObject(), // Convert mongoose document to plain object
      usedTime: formattedUsedTime, // Replace usedTime with formatted string
    };
  });

  return formattedActivities;
};

exports.addUserActivity = async (activityData) => {
  try {
    // Validate userId
    if (!activityData.userId) {
      throw new Error('userId is required');
    }

    // Fetch user details from Firestore
    const userDoc = await firestore.collection('user').doc(activityData.userId).get();

    if (!userDoc.exists) {
      throw new Error('User not found in Firestore');
    }

    const userData = userDoc.data();

    // Remove all spaces from writtenLetterOrWord
    const sanitizedWrittenLetterOrWord = activityData.writtenLetterOrWord.replace(/\s+/g, '');

    // Compare letterOrWord and writtenLetterOrWord for correctness
    const correctness = activityData.letterOrWord === sanitizedWrittenLetterOrWord;

    // Fetch the last activity for the user to determine the roundCount
    const lastActivity = await UserActivity.findOne({ userId: activityData.userId })
      .sort({ date: -1 });

     const roundCount = lastActivity ? lastActivity.roundCount + 1 : 1; 
     const wrongCount = correctness
     ? (lastActivity ? lastActivity.wrongCount : 0) // Keep the same wrongCount if correct
     : (lastActivity ? lastActivity.wrongCount + 1 : 1);

     console.log(roundCount)
    // Include user details and correctness in activity data
    const activity = new UserActivity({
      ...activityData,
      userEmail: userData.email,
      userName: userData.userName,
      correctness: correctness,
      roundCount: roundCount,
      wrongCount: wrongCount,
      writtenLetterOrWord:sanitizedWrittenLetterOrWord 
    });

    console.log('==================================');
    console.log('Processed activityData: ', activity);
    console.log('==================================');

    // Save activity in MongoDB
    return await activity.save();
  } catch (error) {
    console.error('Error adding user activity:', error);
    throw error;
  }
};


