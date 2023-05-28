const ctx_anime = document.getElementById('profileChartAnime');
const ctx_manga = document.getElementById('profileChartManga');
const token = document.querySelector("[name = 'csrfmiddlewaretoken']").value;
const user = document.querySelector("[name = 'user']").value;
labels1 = ["Запланировано", "Смотрю", "Просмотрено", "Отложено", "Брошено"];
labels2 = ["Запланировано", "Читаю", "Прочитано", "Отложено", "Брошено"];

async function getUserListsData(type){
    var data = [];
    if (type == "Anime")
        var apiURLBase = '/api/v1/animelist/';
    else if (type == "Manga")
        var apiURLBase = '/api/v1/mangalist/';
    for (let i = 1; i < 6; i++){
        var apiURL = apiURLBase + '?status=' + i + '&user=' + user;
        try {
        const response = await sendRequest('GET', apiURL, null, token);
        data.push(response.count);
        } catch (error) {
            console.log(error);
        }
    }
    return data;
}
async function createCharts(labels, titleType, label, instance) {
    if (instance) {
        const data = await getUserListsData(titleType);
        const legendColors = [
          'rgb(52, 152, 219)',  // blue
          'rgb(46, 204, 113)',  // green
          'rgb(155, 89, 182)',  // purple
          'rgb(241, 196, 15)',  // yellow
          'rgb(231, 76, 60)'    // red
        ];

        return new Chart(instance, {
          type: 'doughnut', // Изменяем тип на 'doughnut'
          data: {
            labels: labels,
            datasets: [{
              label: label,
              data: data,
              backgroundColor: legendColors
            }]
          },
          options: {
            color: 'rgb(255, 255, 255)',
          }
        });
    }
}

function handleResize() {
  const windowWidth = window.innerWidth;
  const windowHeight = window.innerHeight;
  try{
    if (windowWidth >= 540){
        chart1.resize(500, 500);
        chart2.resize(500, 500);
    }
    else if (windowWidth >=340){
        chart1.resize(300, 300);
        chart2.resize(300, 300);
    }
    else{
        chart1.resize(200, 200);
        chart2.resize(200, 200);
    }
  }catch(error){
    console.log(error);
  }
}

var chart1;
var chart2;

async function initializeCharts() {
  chart1 = await createCharts(labels1, "Anime", "Список аниме", ctx_anime);
  chart2 = await createCharts(labels2, "Manga", "Список манги", ctx_manga);

  window.addEventListener('resize', handleResize);
}

initializeCharts();
