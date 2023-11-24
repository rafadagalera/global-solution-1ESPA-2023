const button = document.querySelector("button");
const inputNome = document.querySelector("#nome");
const inputEmail = document.querySelector("#email");
const inputTexto = document.querySelector('textarea'); 

// criando um elemento p
const pMensagem = document.createElement('p');

const clearForm = () => {
  inputNome.value = '';
  inputEmail.value = '';
  inputTexto.value = '';
}

button.addEventListener("click", function(event) {
  event.preventDefault();

  // validações
  if (inputNome.value.trim() === '') {
    pMensagem.textContent = "Campo obrigatório";
    inputNome.insertAdjacentElement("afterend", pMensagem);
    pMensagem.setAttribute("class", "error");
    return false;
  }

  if (inputEmail.value.trim() === '') { 
    pMensagem.textContent = "Campo obrigatório";
    inputEmail.insertAdjacentElement("afterend", pMensagem);
    pMensagem.setAttribute("class", "error");
    return false;
  }

  if (inputTexto.value.trim() === '') {
    pMensagem.textContent = "Campo obrigatório";
    inputTexto.insertAdjacentElement("afterend", pMensagem);
    pMensagem.setAttribute("class", "error");
    return false;
  }
  

  clearForm();

  alert('Agradecemos o seu contato!')
});
