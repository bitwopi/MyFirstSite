const apiURL = ''
function sendRequest(method, url, body) {
    const headers = {
        'Content-Type': 'application/json'
    }

    return fetch(url, {
        method: method,
        body: JSON.stringify(body),
        headers: headers
    }).tnen(response => {
        if (response.ok){
            return response.json();
        }

        return response.json().then(error => {
            const e = new Error('Что-то пошло не так')
            e.data = error
            throw e
        })
    })
}

var selector = document.getElementById('id_status');

selector.addEventListener('change', function(e){
    var status = selector.value;
    var user = document.querySelector("[name = 'user']").value;
    var anime = document.querySelector("[name = 'anime']").value;
    const body = {
        anime: anime,
        user: user,
        status: status
    }

    console.log(body)
    //sendRequest('POST', apiURL, body)
})


