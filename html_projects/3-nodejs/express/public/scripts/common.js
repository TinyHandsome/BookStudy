$.ajax({
    url: '/api/list',
    success(result){
        let html = '<ul>'

        $.each(result.data, (index, value) => {
            html += '<li>' + value + '</li>'
        })
        
        html += '</ul>'

        $('#list').html(html)
    }
})