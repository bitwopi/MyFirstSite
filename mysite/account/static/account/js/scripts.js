const rates  = document.querySelectorAll("#rate");
const rate_inputs = document.querySelectorAll("#rate-input");
const list_ids = document.querySelectorAll("#list-id");
const token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
const type = document.querySelector("#type");
if (rates && rate_inputs) {
    rates.forEach((rate, i) => {
        rate.addEventListener("mouseover", (e) => {
            rate.classList.add('active');
            rate_inputs[i].classList.add('active');
        })
    })
    rate_inputs.forEach((rate_input, i) => {
        rate_input.addEventListener("change", (e) => {
            last_value = rate_input.value;
        })
        rate_input.addEventListener("mouseleave", (e) => {
            rate_input.classList.remove('active');
            rates[i].classList.remove('active');
            if (type.value == "Anime")
                apiURL = '/api/v1/animelist/' + list_ids[i].value;
            else
                apiURL = '/api/v1/mangalist/' + list_ids[i].value;
            body = {
                rate: rate_input.value,
            }
            console.log(rates[i].innerHTML);
            if (rate_input.value != rates[i].innerHTML)
                sendRequest("PATCH", apiURL, body, token);
                rates[i].innerHTML = rate_input.value;
        })
    })
}


