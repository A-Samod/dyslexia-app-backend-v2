const express = require('express');
const router = express.Router();
const letterController = require('../controllers/letterController');

router.get('/:type', letterController.getLettersByType);

module.exports = router;
