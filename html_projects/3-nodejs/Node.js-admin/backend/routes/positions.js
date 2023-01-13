const express = require('express');
const router = express.Router()

const { add, list, remove, update } = require('../controllers/positions');
const uploadMiddleware =  require('../middlewares/upload');

router.get('/list', list)
// router.post('/add', upload.single('companyLogo'), add)
router.post('/add', uploadMiddleware, add)
router.delete('/remove', remove)
router.patch('/update', uploadMiddleware, update)

module.exports = router