#include <iostream>
#include <string>
using namespace std;

class Car {
    public:
        string brand;
        string model;
        string year;
        string color;

        Car(string x, string y, string z, string m){
            brand = x;
            model = y;
            year = z;
            color = m;
        }

        void honk(){
            cout << "honk honk ! \n";
        }

        void speed(int speed ){
            cout << "The speedometer marks " << speed ;
        }
};

int main(){
    Car myCar("ford","T", "1920","black");

    cout << myCar.brand << " " << myCar.model << " " << myCar.year << " " << "\n";

    myCar.honk();
    myCar.speed(200);

    return 0;
}