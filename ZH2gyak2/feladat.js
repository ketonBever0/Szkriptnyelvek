// Nev: Kurucz Laszlo
// Neptun: Z5RFY1
// h: h373677

function ajandekut(jaratok, jegyek) {
	if (typeof jegyek != "number") return undefined;

	for (let i = 0; i < jaratok.length; i++, jegyek--) {
		if (jegyek == 0) return jaratok[i];
		if (jaratok[i] > jaratok.length) return "Eltevedtunk";
	}

	return jaratok[jaratok.length - 1];
}

// console.log(ajandekut([1, 2, 3], 5));
// console.log(ajandekut([2, -2, 4, 1, 2], 3));

class Kuldetes {
	nev;
	hossz;
	jatekoslimit;
	_nehezsegszintek = [];

	constructor(nev, hossz = 3, jatekoslimit = 3) {
		this.nev = nev;
		this.hossz = hossz;
		this.jatekoslimit = jatekoslimit;
		this._nehezsegszintek = [];
	}

	get nehezsegszintek() {
		return this._nehezsegszintek;
	}

	set nehezsegszintek(arr) {
		if (Array.isArray(arr) && arr.length == this.hossz)
			this._nehezsegszintek = arr;
	}

	ujBoss(diffic) {
		this._nehezsegszintek.push(diffic);
		this.hossz++;
	}

	nehezedo() {
		for (let i = 1; i < this._nehezsegszintek.length; i++) {
			if (this._nehezsegszintek[i - 1] >= this._nehezsegszintek[i])
				return false;
		}
		return true;
	}

	jatek(erok) {
		if (
			this._nehezsegszintek.length == 0 ||
			erok.length > this.jatekoslimit
		)
			return "A jatek nem indithato";

		let sum = 0;
		for (let i = 0; i < erok.length; i++) {
			sum += erok[i];
		}

		let lepes = 0;
		for (let i = 0; i < this._nehezsegszintek.length; i++) {
			if (Math.ceil(sum / erok.length) >= this._nehezsegszintek[i])
				lepes++;
		}

		return lepes == this._nehezsegszintek.length
			? "Kuldetes teljesitve"
			: lepes
	}
}


let k = new Kuldetes('Varazshegy', 3, 4);
k.nehezsegszintek = [20, 25, 30];
console.log(k.nehezedo()); // true
k.ujBoss(40);
// console.log(k.reszletek()); // "Varazshegy kuldetes: 4 lepes, legfeljebb 4 jatekos, nehezseg: 20, 25, 30, 40"
console.log(k.jatek([45, 40, 30, 35])); // 3
console.log(k.jatek([45, 50, 35, 55])); // "Kuldetes teljesitve"
