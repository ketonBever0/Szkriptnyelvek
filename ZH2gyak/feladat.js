// Nev: Vezeteknev Keresztnev
// Neptun: NEP4LF
// h: h123456

function cimkez(str) {
	if (str == null || typeof str != "string" || str.split("_").length == 0)
		return "";
	const kulcsszavak = str.split("_");

	let cimke = str;

	if (cimke.startsWith("x1")) {
		for (let i = 0; i < cimke.length; i++) {
			if (i % 2 == 0) {
				kulcsszavak.splice(i, 1, " ");
			}
		}
		console.log(kulcsszavak);
		cimke = "";
		for (let i = 0; i < kulcsszavak.length; i++) {
			cimke += kulcsszavak[i];
		}
		return cimke.trim();
	} else if (cimke.startsWith("x2")) {
		cimke = cimke.replace("x2", "akcio");
		cimke = cimke.replaceAll("_", " ");
		return cimke;
	} else {
		return str.toUpperCase();
	}
}

// console.log(cimkez('x1_uj_botmixer_szett_asd_dsa')); // "uj szett"
// console.log(cimkez('x2_gumilabda_pottyos_asd')); // "akcio gumilabda pottyos"
// console.log(cimkez('teli_bakancs_44_meret')); // "TELI_BAKANCS"
// console.log(cimkez(42)); // ""

function atlag(arr, korlat) {
	if (!Array.isArray(arr) || arr.length == 0) return null;

	let sum = 0;
	arr.forEach((num) => {
		sum += Math.min(Math.abs(num), korlat);
	});

	return Math.round(sum / arr.length);
}

// console.log(atlag([1, -3, 4], 3)); // 2
// console.log(atlag([2, -3, 4], 3)); // 3
// console.log(atlag([-3, 0, -4, 9], 1)); // 1
// console.log(atlag(4, 7)); // null

class Mozi {
	nev;
	ferohely;
	_nyitva;
	musor = {};

	constructor(nev, ferohely = 50, nyitva = false) {
		this.nev = nev;
		this.ferohely = ferohely;
		this._nyitva = nyitva;
	}

	get nyitva() {
		return this._nyitva;
	}

	set nyitva(val) {
		if (val == true) {
			this._nyitva = ("hetfo" in this.musor) ? true : false;
		} else this._nyitva = val;
	}

	google() {
		let str = "";
		if (this._nyitva) {
			str += `${this.nev} mozi: ${this.ferohely} ferohely `;
			const napok = Object.keys(this.musor);
			napok.forEach((nap) => {
				str += `${nap} `;
			});
			str += "napokon nyitva.";
		} else {
			str += `${this.nev} mozi: ${this.ferohely} ferohely, jelenleg zarva.`;
		}
		return str;
	}

	ujFilm(nap, cim) {
		this.musor = {
			...this.musor,
			[nap]: cim,
		};
	}

    bevetel(jegyar) {
        if (!this._nyitva) return 0;

        let vegosszeg = 0;

        Object.keys(this.musor).forEach((film) => {
            const hozzaad = (this.ferohely - this.musor[film].length) * jegyar;
            // console.log(this.musor[film].length)
            vegosszeg += (film == "pentek") ? (hozzaad * 0.2) : hozzaad;
        })
        return vegosszeg;
    }

    felujit() {
        this._nyitva = false;
        this.ferohely = Math.round(this.ferohely * 1.3);
        // this.musor[Object.keys(this.musor)[0]] = "";
        delete this.musor[Object.keys(this.musor)[0]];
    }

}

// let m2 = new Mozi('Kulvarosi', 40);
// m2.ujFilm('szerda', 'Deadpool & Wolverine');
// m2._nyitva = false;
// console.log(m2.google());

// let m = new Mozi('Belvarosi', 40);
// m.ujFilm('szerda', 'Deadpool & Wolverine');
// m.ujFilm('hetfo', 'Lego movie');
// m.nyitva = true;
// console.log(m.musor); // { szerda: 'Deadpool & Wolverine', hetfo: 'Lego movie' }
// console.log(m.bevetel(200)); // 9600
// m.felujit();
// m.ujFilm('kedd', 'Garfield movie');
// m.ujFilm('pentek', 'Zootopia 2');
// m.nyitva = true;
// console.log(m.musor);
// console.log(m.google()); // "Belvarosi mozi: 52 ferohely, hetfo kedd pentek napokon nyitva"
// console.log(m.bevetel(200)); // 22720
// console.log(m.ferohely);
