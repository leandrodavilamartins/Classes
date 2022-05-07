class ClubCard {
    constructor(valor){
        this.naipe = 'Clubs';
        this.valor = valor;
    }
}

class SpadeCard {
    constructor(valor){
        this.naipe = 'Spades';
        this.valor = valor;
    }
}

class DiamondCard {
    constructor(valor){
        this.naipe = 'Diamond';
        this.valor = valor;
    }
}

class HeartCard {
    constructor(valor){
        this.naipe = 'Hearts';
        this.valor = valor;
    }
}


let valor = [1,2,3,4,5,6,7,8,9,10];

let cards = [];

valor.forEach( v => {
    let clubcard = new ClubCard(v);
    let diamondcard = new DiamondCard(v);
    let spadeCard = new SpadeCard(v);
    let heartCard = new HeartCard(v);
    cards.push([clubcard, diamondcard, spadeCard, heartCard]);
});

//console.log(cards);
console.log(cards[0][0].naipe);
console.log(cards[0][0].valor);

