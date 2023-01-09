class Page {
    constructor() {
        this.curPage = 1
        this.pageSize = 3,
        this.curRoute = '#/index'
    }

    setCurPage(curPage) {
        this.curPage = curPage
    }

    reset(){
        this.curPage = 1
        this.pageSize = 3
    }

    setCurRoute(route) {
        this.curRoute = route
    }
}

export default new Page()