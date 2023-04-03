let numIndex = document.getElementsByTagName("li").length
console.log(numIndex);

let elementoEntrada = document.getElementsByTagName("li")[numIndex - 1];
let horaEntrada = elementoEntrada.textContent;
let horario = horaEntrada.slice(1, 6);
let stringHorario = horario.split(":");
let horaEn = parseInt(stringHorario[0]);
let minutosEn = parseInt(stringHorario[1]);

let turno = document.querySelector("#turno__trabalho");


let horarioSaida = turno.textContent.slice(13);
let listSaida = horarioSaida.split(":");

let previsaoSaida = 0


if(horaEn < 12) {
    horaEn = horaEn;
} else {
    // horaEn = horaEn + 9;
    // previsaoSaida = horaEn + parseInt(listSaida);
    previsaoSaida = horaEn + 9;
}


if (horaEn < 9) {
    console.log("Você está adiantado!");
} else if ( horaEn > 18) {
    console.log("Seu turno acabou! Hora de descansar!");
} else {
    console.log("Você está atrasado!");
}

let timer = document.querySelector("#relogio__user__profile")

let minutosSaida;

if (minutosEn < 10){
    minutosSaida = "0" + minutosEn.toString()
} else {
    minutosSaida = minutosEn.toString()
}

timer.innerHTML = previsaoSaida.toString() + ":" + minutosSaida;

alert(previsaoSaida);