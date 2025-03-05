// Nev: Kurucz Laszlo
// Neptun: Z5RFY1
// h: h373677

function tokeletes(num) {
	if (typeof num != "number" || num == 0) return false;
	// console.log(num);
	let osztok = [];

	for (i = num - 1; i > 0; i--) {
		if (num % i == 0) osztok.push(i);
	}

	let osszeg = 0;

	osztok.forEach((val) => {
		osszeg += val;
	});
	return osszeg == num;
}

// console.log(tokeleses(Math.pow(2, 6) * (Math.pow(2, 7) - 1)));

class Webbongeszo {
	lapok = [];
	memoria;
	_memoriafogyasztas = 0;

	constructor(memoria = 8192) {
		this.memoria = memoria;
	}

	get memoriafogyasztas() {
		return this._memoriafogyasztas;
	}

	set memoriafogyasztas(val) {
		this._memoriafogyasztas = Math.min(Math.max(0, val), this.memoria);
	}

	ujLap(url) {
		this.lapok.push(url);
		this.memoriafogyasztas =
			this.memoriafogyasztas + Math.floor(Math.random() * 1401) + 100;
	}

	lapBezar() {
		this.lapok.pop();
		this.memoriafogyasztas =
			this.memoriafogyasztas - (Math.floor(Math.random() * 971) + 30);
	}

	panik() {
		this.lapok.splice(0, this.lapok.length);
		this.memoriafogyasztas = 0;
	}
}

// let edge = new Webbongeszo(1000);
// edge.memoriafogyasztas = 1599;
// console.log(edge.memoriafogyasztas);
// edge.ujLap("1");
// edge.ujLap("2");
// edge.ujLap("3");
// console.log(edge.memoriafogyasztas);
// edge.lapBezar();
// edge.ujLap("11");
// // edge.panik();
// console.log(edge.memoriafogyasztas);
// console.log(edge.lapok);

// console.log(Math.min(Math.max(0, 1001), 1000));
console.log(Math.floor(Math.random() * (1500 - 300 + 1) + 300));
