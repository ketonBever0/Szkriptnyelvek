// Nev: Kurucz László
// Neptun: Z5RFY1
// h: h373677

function matek(param) {
	if (param == undefined || param == null) return 0;
	else if (typeof param == "string") return 1;
	else if (Number.isInteger(param))
		return param % 2 == 0 ? Math.pow(param, param) : Math.pow(param - 1, 2);
	else return null;
}

// console.log(matek(8));
