// Nev: Kurucz Laszlo
// Neptun: Z5RFY1
// h: h373677

function clear(arr) {
	if (!arr) return 0;
	let newArr = [];

	arr.forEach((val) => {
        if (!val) return;
		switch (typeof val) {
			case "number":
				newArr.push(val);
				break;
			case "string":
				if (val.match(/[A-Z]|[a-z]/g).length > 0)
					newArr.push(val.substring(0, 2).toUpperCase());
				break;
		}
	});

	return newArr.reverse();
}

console.log(clear([2, 5, 3, "heyho", null, 7]));
