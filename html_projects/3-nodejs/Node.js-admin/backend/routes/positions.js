const express = require('express');
const router = express.Router()

const { add, list } = require('../controllers/positions');

router.get('/list', list)
router.post('/add', add)

module.exports = router