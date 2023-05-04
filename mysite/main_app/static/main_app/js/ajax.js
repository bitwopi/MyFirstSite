var apiURL = '/api/v1/animelist/'
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
var anime_list_id = document.querySelector("[name = 'anime_list_id']")

selector.addEventListener('change', function(e){
    var method = 'POST'
    var status = selector.value;
    var user = document.querySelector("[name = 'user']").value;
    var anime = document.querySelector("[name = 'anime']").value;
    var token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
    var body = {}
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

    sendRequest(method, apiURL, body, token)
})


