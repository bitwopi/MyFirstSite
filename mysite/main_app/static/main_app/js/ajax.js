async function sendRequest(method, url, body, token) {
    const headers = {
        'X-CSRFTOKEN': token,
    };

    let request;
    let requestBody;
    if (body) {
          if (body instanceof FormData) {
            requestBody = body;
          } else {
            requestBody = JSON.stringify(body);
            headers['Content-Type'] = 'application/json';
          }
        request = {
            method: method,
            body: requestBody,
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
        let method = 'POST'
        const status = selector.value;
        const user = document.querySelector("[name = 'user']").value;
        const token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
        let body = {}
        try{
            const anime = document.querySelector("[name = 'anime']").value;
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
        } catch(e) {
            console.log(e.message)
            const manga = document.querySelector("[name = 'manga']").value;
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
        console.log(list_id);
        sendRequest(method, apiURL, body, token);
    })
}

