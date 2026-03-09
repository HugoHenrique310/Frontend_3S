// let nome=prompt("Como voce chama?")
// // "Hugo" igual a '' verifica o valor
// // === Verifica o tipo e valor
// // 1 == '1' é igual para o java
// if (nome === '') {
//     alert("Recarregue a página")
// }
// let correto=confirm("Você se chama" + nome  + "?")
// if (correto) {
//     alert(nome +  "Bem vindo ao Site de cursos")
// } else {
//     alert("Recarregue a página")
// }

function limpaInputsLogin() {
    const inputEmail = document.getElementById("input_email")
    const inputSenha = document.getElementById("input_senha")

    inputEmail.value = ""
    inputSenha.value = ""

}


document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById("form_login")

    formLogin.addEventListener("submit", function (event) {
        // Pegar os dois inputs do formulario
        const inputEmail = document.getElementById("input_email")
        const inputSenha = document.getElementById("input_senha")

        let temErro = false

        // Verificar se os inputs estão vazios

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }


        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // Evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })

})
