// 

const UserActivity = require('../models/userActivityModel');
const firestore = require('../config/firebaseConfig');

exports.fetchUserActivities = async (userId) => {
  return await UserActivity.find({userId}, null, {sort: {date: -1}});
};

// exports.addUserActivity = async (activityData) => {
//   const activity = new UserActivity(activityData);
//   return await activity.save();
// };


//const UserActivity = require('../models/userActivityModel');

exports.addUserActivity = async (activityData) => {
  try {
    console.log('activityData >>>', activityData.userId);
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

    // Include user details in activity data
    const activity = new UserActivity({
      ...activityData,
      userEmail: userData.email,
      userName: userData.userName,
    });

    console.log('Received activityData: >>>>', activityData);


    // Save activity in MongoDB
    return await activity.save();
  } catch (error) {
    console.error('Error adding user activity:', error);
    throw error;
  }
};


