#include <iostream>

int main() {

    std::string response = "";
    while (response != "y") {
        std::cout << "Would you like to play 100? y/n ";
        std::cin >> response;
    }

    while (response == "y") {
        int v1 = 0, v2 = 0, v3 = 0, v4 = 0;
        while (v1 <= 0 || v1 >= 20) {
            std::cout << "Enter a number below 20: ";
            std::cin >> v1;
            if (v1 >= 20) {
                std::cout << "That's too high, try again \n";
            } else if (v1 <= 0) {
                std::cout << "That's not enough, try again \n";
            }
        }
        while (v2 + v1 <= 100) {
            v2 = v2 + v1;
            v3++;
        }

        
        std::cout << "Your number goes into 100 " << v3 << " times\n";
        if (v2 < 100) {
            v4 = 100 - v2;
            std::cout << "The remainder is " << v4;
        }
        std::cout << "\nPlay again? y/n ";
        std::cin >> response;
    }
}