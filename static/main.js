$(document).ready(function() {
    const request = $.ajax({
        type: "GET",
        url: "/data",  //путь к def data()
        data: {"name": ""},
        dataType: "html"
    });
    // Парсинг json-переменной
    request.done(function(JSON_array) {
        let array_data = JSON.parse(JSON_array)["array"]

        // Вывод данных
        $("#out").text(array_data)
    });
});