$.ajax({
    url: '/api/list',
    success(result) {
        let templateStr = 
        `
            <ul>
                {{each data}}
                    <li>{{$value}}</li>
                {{/each}}
            </ul>
        `

        // let html = '<ul>'
        // $.each(result.data, (index, value) => {
        //     html += '<li>' + value + '</li>'
        // })
        // html += '</ul>'

        let html = template.render(templateStr,
            { data: result.data }
        )

        $('#list').html(html)
    }
})