const express = require('express');
const router = express.Router()

const { add, list, remove, update, listone } = require('../controllers/positions');
const uploadMiddleware =  require('../middlewares/upload');

router.get('/list', list)
// router.post('/add', upload.single('companyLogo'), add)
router.post('/add', uploadMiddleware, add)
router.delete('/remove', remove)
router.patch('/update', uploadMiddleware, update)
router.post('/listone', listone)

module.exports = router