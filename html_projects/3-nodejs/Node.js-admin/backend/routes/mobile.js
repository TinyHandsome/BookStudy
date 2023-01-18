var express = require('express');
var router = express.Router();

const { positions } = require('../controllers/mobile');

/* GET users listing. */
router.get('/positions', positions)

module.exports = router;
