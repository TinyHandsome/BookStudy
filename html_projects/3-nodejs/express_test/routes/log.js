var log4js = require('log4js')

log4js.configure({
    appenders: {cheese: {type: "file", filename: "cheese.log"}},
    categories: {default: {appenders: ["cheese"], level: "error"}}
})

var logger = log4js.getLogger('cheese')
logger.level = "debug"

module.exports = logger