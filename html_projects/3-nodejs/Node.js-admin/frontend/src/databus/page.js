class Page {
    constructor() {
        this.curPage = 1
        this.pageSize = 4
    }

    setCurPage(curPage) {
        this.curPage = curPage
    }
}

export default new Page()