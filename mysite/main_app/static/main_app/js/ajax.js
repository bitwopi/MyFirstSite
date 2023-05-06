function sendRequest(method, url, body, token) {
    const headers = {
        'Content-Type': 'application/json',
        'X-CSRFTOKEN': token,
    };

    return fetch(url, {
        method: method,
        body: JSON.stringify(body),
        headers: headers
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        anime_list_id.value = data['id']
    })
    .catch((e) => console.log(e.message))
};

var selector = document.getElementById('id_status');

selector.addEventListener('change', function(e){
    var method = 'POST'
    var status = selector.value;
    var user = document.querySelector("[name = 'user']").value;
    var token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
    var body = {}
    try{
        var anime = document.querySelector("[name = 'anime']").value;
        var anime_list_id = document.querySelector("[name = 'anime_list_id']")
        var apiURL = '/api/v1/animelist/'
        if (anime_list_id.value != ''){
        body = { status: status, }
        method = 'PATCH'
        apiURL += anime_list_id.value
        console.log(apiURL)
        }else{
            body = {
                status: status,
                anime: anime,
                user: user,
            }
        }
    }catch{
        var manga = document.querySelector("[name = 'manga']").value;
        var manga_list_id = document.querySelector("[name = 'manga_list_id']")
        var apiURL = '/api/v1/mangalist/'
        if (manga_list_id.value != ''){
        body = { status: status, }
        method = 'PATCH'
        apiURL += manga_list_id.value
        console.log(apiURL)
        }else{
            body = {
                status: status,
                manga: manga,
                user: user,
            }
        }
    }

    sendRequest(method, apiURL, body, token)
})
