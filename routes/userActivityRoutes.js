// 
const express = require('express');
const router = express.Router();
const userActivityController = require('../controllers/userActivityController');

router.get('/activities/:userId', userActivityController.getAllActivities);
router.post('/submit', userActivityController.submitActivity);

module.exports = router;
