// Nev: Vezeteknev Keresztnev
// Neptun: NEP4LF
// h: h123456



class Nyuszi {
    _repa;
    vendegek = [];

    constructor(repa = 0) {
        this._repa = repa
    }

    get repa() {
        return this._repa;
    }

    ultet(mennyi) {
        if (mennyi == null) this._repa += 1;
        else this._repa += mennyi;
    }

    vendeg (kit) {
        if (typeof kit == "string") this.vendegek.push(kit);
    }

    etet () {
        let i = 0;
        while (this.repa > 0 && this.vendegek.length > 0) {
            this._repa--;
            this.vendegek.shift();
            i++;
        }
    }


}


// // nincs répája Nyuszinak.
// var nyusz = new Nyuszi(0);
// //ültet egy répát.
// nyusz.ultet(1);
// console.log(nyusz.repa); // 1.
// console.log(nyusz.vendegek); //még nincs vendége az eredmény [].
// nyusz.vendeg('Robert Gida'); // Róbert Gida megérkezik Nyuszihoz.
// nyusz.vendeg('Malacka'); // Malacka megérkezik Nyuszihoz.
// console.log(nyusz.vendegek); ['Robert Gida', 'Malacka']
// nyusz.etet(); // Mivel van egy 1 répa, Robert Gida kap egyet és utána haza megy.
// // Malackának már nem jutott répa, ezért neki várnia kell.
// console.log(nyusz.repa) // 0
// console.log(nyusz.vendegek); // ['Malacka']
