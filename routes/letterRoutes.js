const express = require('express');
const router = express.Router();
const letterController = require('../controllers/letterController');

router.get('/:type', letterController.getLettersByType);
router.post('/add', letterController.addLetter);

module.exports = router;
