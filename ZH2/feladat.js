// Nev: Kurucz Laszlo
// Neptun: Z5RFY1
// h: h373677



function nemoszto(num1, num2) {

    if (typeof num1 != "number" || typeof num2 != "number") return -1;
    if (num2 > num1) return -2;

    let osztoi = 0;
    for (let i = 1; i < num2; i++) {
        if (num1 % i == num2) osztoi++;
    }
    return osztoi;
}

// console.log(nemoszto(25, 10));


class Metro {

    ajtok;
    megallok = [];
    aktualisMegallo;
    _menetirany;


    constructor(ajtokSzama = 4, megallok =  ['KĹbĂĄnya-Kispest', 'KĂĄlvin tĂŠr', 'Ferenciek tere', 'Ăjpest-kĂśzpont'], _menetirany = true) {
        this.ajtok = ajtokSzama;
        this.megallok = megallok;
        this._menetirany = _menetirany;
        this.aktualisMegallo = _menetirany ? 0 : this.megallok.length - 1;
    }

    get megallo() {
        return this.megallok[this.aktualisMegallo];
    }

    get menetirany() {
        return this._menetirany;
    }

    set menetirany(val) {
        if (this.aktualisMegallo == 0) this._menetirany = true;
        else if (this.aktualisMegallo == this.megallok.length - 1) this._menetirany = false;
        else this._menetirany = val;
    }




}



