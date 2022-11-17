var express = require('express');
var router = express.Router();

const { signup, list, remove } = require('../controllers/users');

/* GET users listing. */
router.post('/', signup)
router.get('/', list)
router.delete('/', remove)

module.exports = router;
