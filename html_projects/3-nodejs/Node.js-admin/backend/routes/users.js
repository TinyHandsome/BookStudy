var express = require('express');
var router = express.Router();

const { signup, list, remove, signin } = require('../controllers/users');

/* GET users listing. */
router.get('/', list)
router.delete('/', remove)

router.post('/', signup)
router.post('/signin', signin)

module.exports = router;
