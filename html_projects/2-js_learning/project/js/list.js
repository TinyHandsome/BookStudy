// 列表页的逻辑代码
// 1. 请求分类列表，渲染分类位置内容
getCateList()
function getCateList() {
    // 1.1 直接发送请求
    $.get('xxx', res => {
        console.log(res);

        // 1.2 渲染分类内容
        let str = `<li class="active">全部</li>`
        res.list.forEach(item => {
            str += `<li>${ item }</li>`
        })
        $('.category').html(str)
    })
}