const http = ({
    url,
    type = 'get',
    data = {}
}) => {
    return new Promise((resolve, reject) => {
        $.ajax({
            url,
            dataType: 'json',
            type,
            data,
            headers: {
                'X-Access-Token': localStorage.getItem('lg-token') || ''
            },
            success(result, textStatus, jqXHR) {
                resolve({
                    result,
                    textStatus,
                    jqXHR
                })
            },
            error(err) {
                reject(err.message)
            }
        })
    })
}

export default http