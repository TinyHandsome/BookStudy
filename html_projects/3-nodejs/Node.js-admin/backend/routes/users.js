var express = require('express');
var router = express.Router();

const { signup, list } = require('../controllers/users');

/* GET users listing. */
router.post('/signup', signup)
router.get('/list', list)

module.exports = router;
