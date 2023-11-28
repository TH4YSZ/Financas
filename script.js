document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://127.0.0.1:5500/index.html';
    const tabela = document.querySelector(".tabela-js");

    axios.get(`${apiUrl}/list`)
        .then(function (resposta) {
            getData(resposta.data);
        })
        .catch(function (error) {
            console.error(error);
        });
});
