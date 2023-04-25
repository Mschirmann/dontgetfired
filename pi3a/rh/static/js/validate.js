const submit = document.getElementById("submit");

submit.addEventListener("click", validate);

function validate(e) {
  e.preventDefault();

  const cpf = document.getElementById("cpf");
  const nome = document.getElementById("name");
  const sobrenome = document.getElementById("lastname");
  const senha = document.getElementById("pass");
  const senhaconf = document.getElementById("pass_conf");

  let validoForm = false
  let validoCpf = false;
  let validoNome = false;
  let validoSobrenome = false;
  let validoPass = false;
  let validoPAssConf = false;
  const err = document.getElementById("error");
  const err1 = document.getElementById("error1");
  const err2= document.getElementById("error2");
  const err3 = document.getElementById("error3");
  const err4 = document.getElementById("error4");


// cpf
let num = /^\d+$/.test(cpf.value)
console.log(num)
  if(cpf.value.length == 11 && num){
    console.log(cpf.value.length);
    err.classList.remove("visible");
    cpf.classList.remove("invalid");
    err.setAttribute("aria-hidden", true);
    err.setAttribute("aria-invalid", false);
    validoCpf = true;
  } 

  if (!cpf.value.length < 11 && !num) {
    // const err = document.getElementById("error");
    err.classList.add("visible");
    cpf.classList.add("invalid");
    err.setAttribute("aria-hidden", false);
    err.setAttribute("aria-invalid", true);
    validoCpf = false
  }

  // nome
  if(nome.value.match(/^\[A-Za-Z]+$/)){
    console.log(cpf.value.length);
    err1.classList.remove("visible");
    nome.classList.remove("invalid");
    err1.setAttribute("aria-hidden", true);
    err1.setAttribute("aria-invalid", false);
    validoNome = true;
  }

  if (!nome.value.match(/^\[A-Za-Z]+$/)) {
    // const err = document.getElementById("error");
    err1.classList.add("visible");
    nome.classList.add("invalid");
    err1.setAttribute("aria-hidden", false);
    err1.setAttribute("aria-invalid", true);
    validoNome = false
  }


  // sobrenome
  if(sobrenome.value.length < 2){
    err2.classList.remove("visible");
    sobrenome.classList.remove("invalid");
    err2.setAttribute("aria-hidden", true);
    err2.setAttribute("aria-invalid", false);
    validoSobrenome = true;
  }

  if (!sobrenome.value.length < 2) {
    // const err = document.getElementById("error");
    err2.classList.add("visible");
    sobrenome.classList.add("invalid");
    err2.setAttribute("aria-hidden", false);
    err2.setAttribute("aria-invalid", true);
    validoSobrenome = false
  }


  //senha
  if(senha.value.length >= 8){
    err3.classList.remove("visible");
    senha.classList.remove("invalid");
    err3.setAttribute("aria-hidden", true);
    err3.setAttribute("aria-invalid", false);
    validoPass = true;
  }

  if (!senha.value.length < 8) {
    // const err = document.getElementById("error");
    err3.classList.add("visible");
    senha.classList.add("invalid");
    err3.setAttribute("aria-hidden", false);
    err3.setAttribute("aria-invalid", true);
    validoPass = false
  }

  // senha conf
  if(senhaconf.value.length == senha.value.length && senhaconf.value === senha.value){
    err4.classList.remove("visible");
    senhaconf.classList.remove("invalid");
    err4.setAttribute("aria-hidden", true);
    err4.setAttribute("aria-invalid", false);
    validoPAssConf = true;
  }

  if (!senhaconf.value.length !== senha.value.length && senhaconf.value !== senha.value ) {
    err4.classList.add("visible");
    senhaconf.classList.add("invalid");
    err4.setAttribute("aria-hidden", false);
    err4.setAttribute("aria-invalid", true);
    validoPAssConf = false
  }
  

  if (validoCpf && validoNome && validoSobrenome && validoPass && validoPAssConf){
    validoForm = true
  }

  return validoForm;
}

function isNumber(valor){
    // valor = parseInt(valor)
    // return /^\d+$/.test(valor)
    let r = new RegExp(/^[0-9a-zA-Z]{11}$/g)
    return r.test(valor)
}
