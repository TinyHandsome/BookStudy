import indexPageHeaderTpl from '../views/index-pageheader.art'

const pageHeader = () => {
    const nav = {
        '#/index/users': {
            mainNav: '用户管理',
            subNav: '用户列表'
        },
        '#/index/positions': {
            mainNav: '职位管理',
            subNav: '职位列表'
        }
    }
    const hash = location.hash
    const html = indexPageHeaderTpl({
        mainNav: nav[hash]['mainNav'],
        subNav: nav[hash]['subNav']
    })
    $('#content').before(html)
}

export default pageHeader