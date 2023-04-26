const submit = document.getElementById("submit");

submit.addEventListener("click", validate);


function validate(e) {
  e.preventDefault();

  const cpf = document.getElementById("cpf").value;
  const nome = document.getElementById("name").value;
  const sobrenome = document.getElementById("lastname").value;
  const senha = document.getElementById("pass").value;
  const senhaConf = document.getElementById("pass_conf").value;

  validateCPF(cpf)
  validateNome(nome)
  validateSobrenome(sobrenome)
  validateSenha(senha)
  validateSenhaConf(senhaConf)

  // return validoForm;
}

function validateCPF(cpf) {
  if (cpf === "") {
    document.getElementById("cpfInvalido").style.display = "block";
    return false;
  } else if (/^[0-9]{11}/.test(cpf)) {
    document.getElementById("cpfInvalido").style.display = "none";
    return false;
  }
  return true;
}

function validateNome(name) {
  if (name === "") {
    document.getElementById("nameInvalido").style.display = "block";
    return false;
  } else if (/^[A-Z][a-z]*/.test(name)) {
    document.getElementById("nameInvalido").style.display = "none";
    return false;
  }
  return true;
}

function validateSobrenome(sobrenome) {
  if (sobrenome === "") {
    document.getElementById("sobrenomeInvalido").style.display = "block";
    return false;
  } else if (/^[A-Z][a-z]*/.test(sobrenome)) {
    document.getElementById("sobrenomeInvalido").style.display = "none";
    return false;
  }
  return true;
}


function validateSenha(senha) {
  if (senha === "") {
    document.getElementById("senhaInvalida").style.display = "block";
    return false;
  } else if (/[A-Za-z0-9]{8}$/.test(senha)) {
    document.getElementById("senhaInvalida").style.display = "none";
    return false;
  }
  return true;
}



function validateSenhaConf(senhaConf) {
  const senha = document.getElementById("pass").value
  console.log(senhaConf);
  console.log(senha);
  if (senhaConf === "" || senhaConf !== senha) {
    document.getElementById("senhaConfInvalida").style.display = "block";
    return false;
  }
   else if (/[A-Za-z0-9]{8}$/.test(senhaConf)) {
    document.getElementById("senhaConfInvalida").style.display = "none";
    return false;
  }
  return true;
}