var express = require('express');
var router = express.Router();
var log4js = require('log4js')

log4js.configure({
    appenders: {cheese: {type: "file", filename: "cheese.log"}},
    categories: {default: {appenders: ["cheese"], level: "error"}}
})

var logger = log4js.getLogger('cheese')
logger.level = "debug"

module.exports = logger

/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index', { title: 'Express' });
});

router.post('/data', (req, res, next) => {
    logger.debug(req.body)
    res.send('ok')
})

module.exports = router;
