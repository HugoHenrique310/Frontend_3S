async function getGato() {
    let resultado = await fetch("https://api.thecatapi.com/v1/images/search")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_gato(dados)
    }
}

function render_gato(dados) {
    let urlImg = dados[0].url
    const imggato = document.getElementById('img-gato')
    const icongato = document.getElementById('icon-gato')

    icongato.style.display = "none"
    imggato.style.display = "block"
    imggato.src = urlImg
}




async function getCachorro() {
    let resultado = await fetch("https://api.thedogapi.com/v1/images/search")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_cachorro(dados)
    }
}

function render_cachorro(dados) {
    let urlImg = dados[0].url
    const imgcachorro = document.getElementById('img-cachorro')
    const iconcachorro = document.getElementById('icon-cachorro')

    iconcachorro.style.display = "none"
    imgcachorro.style.display = "block"
    imgcachorro.src = urlImg
}




async function getRaposa() {
    let resultado = await fetch("https://randomfox.ca/floof")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_raposa(dados)
    }
}

function render_raposa(dados) {
    let urlImg = dados[0].url
    const imgraposa = document.getElementById('img-raposa')
    const iconraposa = document.getElementById('icon-raposa')

    iconraposa.style.display = "none"
    imgraposa.style.display = "block"
    imgraposa.src = urlImg
}