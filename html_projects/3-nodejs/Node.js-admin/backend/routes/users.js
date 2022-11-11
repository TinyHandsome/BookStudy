var express = require('express');
var router = express.Router();

const { signup } = require('../controllers/users');

/* GET users listing. */
router.post('/signup', signup);

module.exports = router;
