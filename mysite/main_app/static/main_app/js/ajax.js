async function sendRequest(method, url, body, token) {
    const headers = {
        'Content-Type': 'application/json',
        'X-CSRFTOKEN': token,
    };

    let request;
    if (body) {
        request = {
            method: method,
            body: JSON.stringify(body),
            headers: headers
        };
    } else {
        request = {
            method: method,
            headers: headers
        };
    }

    try {
        const response = await fetch(url, request);
        const data = await response.json();
        console.log(data);

        if (list_id) {
            list_id.value = data['id'];
        }

        return data;
    } catch (error) {
        console.log(error.message);
    }
};

var selector = document.getElementById('id_status');
var list_id;
if(selector){
    selector.addEventListener('change', function(e){
        var method = 'POST'
        var status = selector.value;
        var user = document.querySelector("[name = 'user']").value;
        var token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
        var body = {}
        try{
            var anime = document.querySelector("[name = 'anime']").value;
            if (anime == null){
                throw new Exception('anime is None')
            }
            list_id = document.querySelector("[name = 'anime_list_id']");
            var apiURL = '/api/v1/animelist/'
            if (list_id.value != ''){
            body = { status: status, }
            method = 'PATCH'
            apiURL += list_id.value
            console.log(apiURL)
            }else{
                body = {
                    status: status,
                    anime: anime,
                    user: user,
                }
            }
        }catch(e){
            console.log(e.message)
            var manga = document.querySelector("[name = 'manga']").value;
            list_id = document.querySelector("[name = 'manga_list_id']")
            var apiURL = '/api/v1/mangalist/'
            if (list_id.value != ''){
            body = { status: status, }
            method = 'PATCH'
            apiURL += list_id.value
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
}

