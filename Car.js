class Car {
    constructor(brand,model,year,color){
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.color = color;
    }

    honk(){
        console.log('honk honk!');
    }
}

let myCar01 = new Car('ford', 'T', '1920','black');

console.log(myCar01);
myCar01.honk();