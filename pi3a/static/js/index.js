let numIndex = document.getElementsByTagName("li").length;
let elementoEntrada = document.getElementsByTagName("li")[numIndex - 1];
let horaEntrada = elementoEntrada.textContent;
let horario = horaEntrada.slice(1, 6);
let stringHorario = horario.split(":");
let horaEn = parseInt(stringHorario[0]);
let minutosEn = parseInt(stringHorario[1]);
let turno = document.querySelector("#turno__trabalho");
let horarioSaida = turno.textContent.slice(13);
let listSaida = horarioSaida.split(":");

let previsaoSaida = 0;

if (horaEn < 12) {
  previsaoSaida = horaEn + 9;
} else {
  previsaoSaida = horaEn + 9;
  if (previsaoSaida > 24) {
    previsaoSaida = previsaoSaida - 24;
  }
}

if (horaEn <= 8 && minutosEn < 50) {
  alert("Você está adiantado!");
} else if ((horaEn <= 8 && minutosEn > 55) || (horaEn == 9 && minutosEn == 0)) {
  alert("Bem-Vind(o/a)!");
}
if (horaEn > 18) {
  alert("Seu turno acabou! Hora de descansar!");
} else if ( horaEn > 9 || horaEn < 18 ){
  alert("Você está atrasado!");
}

let timer = document.querySelector("#relogio__user__profile");

let minutosSaida;

if (minutosEn < 10) {
  minutosSaida = "0" + minutosEn.toString();
} else {
  minutosSaida = minutosEn.toString();
}

timer.innerHTML = previsaoSaida.toString() + ":" + minutosSaida;