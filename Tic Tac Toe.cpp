#include <iostream>
#include <vector>

std::vector<std::string> grid_line0 = {" " ," ", "a", " ", "b", " ", "c"};
std::vector<std::string> grid_line1 = {"1" ," ", "_", "|", "_", "|", "_"};
std::vector<std::string> grid_line2 = {"2" ," ", "_", "|", "_", "|", "_"};
std::vector<std::string> grid_line3 = {"3" ," ", " ", "|", " ", "|", " "};
std::string p1_piece = "X";
std::string p2_piece = "O";
bool p1_on = false;
bool p2_on = false;
bool winner = false;
bool play = true;

void grid() {

    for (int i = 0; i < grid_line0.size(); i++) {
        std::cout << grid_line0[i];
    }
    std::cout << "\n";
    for (int i = 0; i < grid_line1.size(); i++) {
        std::cout << grid_line1[i];
    }
    std::cout << "\n";
    for (int i = 0; i < grid_line2.size(); i++) {
        std::cout << grid_line2[i];
    }
    std::cout << "\n";
    for (int i = 0; i < grid_line3.size(); i++) {
        std::cout << grid_line3[i];
    }
    std::cout << "\n";
}

void player_1() {

    p1_on = true;
    std::string p1_turn = "";
    std::cout << "Player 1 - please type where you'd like to place your X: ";
    std::cin >> p1_turn;
    while (p1_on == true)
        if (p1_turn == "a1" && grid_line1[2] != p1_piece && grid_line1[2] != p2_piece) {
            grid_line1[2] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "a2" && grid_line2[2] != p1_piece && grid_line2[2] != p2_piece) {
            grid_line2[2] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "a3" && grid_line3[2] != p1_piece && grid_line3[2] != p2_piece) {
            grid_line3[2] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "b1" && grid_line1[4] != p1_piece && grid_line1[4] != p2_piece) {
            grid_line1[4] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "b2" && grid_line2[4] != p1_piece && grid_line2[4] != p2_piece) {
            grid_line2[4] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "b3" && grid_line3[4] != p1_piece && grid_line3[4] != p2_piece) {
            grid_line3[4] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "c1" && grid_line1[6] != p1_piece && grid_line1[6] != p2_piece) {
            grid_line1[6] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "c2" && grid_line2[6] != p1_piece && grid_line2[6] != p2_piece) {
            grid_line2[6] = p1_piece;
            p1_on = false;
        } else if (p1_turn == "c3" && grid_line3[6] != p1_piece && grid_line3[6] != p2_piece) {
            grid_line3[6] = p1_piece;
            p1_on = false;
        } else {
            std::cout << "Oops, try a different spot!\n";
            player_1();
        }

}

void player_2() {

    p2_on = true;
    std::string p2_turn = "";
    std::cout << "Player 2 - please type where you'd like to place your O: ";
    std::cin >> p2_turn;
    while (p2_on == true)
        if (p2_turn == "a1" && grid_line1[2] != p1_piece && grid_line1[2] != p2_piece) {
            grid_line1[2] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "a2" && grid_line2[2] != p1_piece && grid_line2[2] != p2_piece) {
            grid_line2[2] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "a3" && grid_line3[2] != p1_piece && grid_line3[2] != p2_piece) {
            grid_line3[2] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "b1" && grid_line1[4] != p1_piece && grid_line1[4] != p2_piece) {
            grid_line1[4] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "b2" && grid_line2[4] != p1_piece && grid_line2[4] != p2_piece) {
            grid_line2[4] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "b3" && grid_line3[4] != p1_piece && grid_line3[4] != p2_piece) {
            grid_line3[4] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "c1" && grid_line1[6] != p1_piece && grid_line1[6] != p2_piece) {
            grid_line1[6] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "c2" && grid_line2[6] != p1_piece && grid_line2[6] != p2_piece) {
            grid_line2[6] = p2_piece;
            p2_on = false;
        } else if (p2_turn == "c3" && grid_line3[6] != p1_piece && grid_line3[6] != p2_piece) {
            grid_line3[6] = p2_piece;
            p2_on = false;
        } else {
            std::cout << "Oops, try a different spot!\n";
            player_2();
        }

}

void win_condition() {

    if (grid_line1[2] == grid_line1[4] && grid_line1[4] == grid_line1[6]) {
        if (grid_line1[2] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line1[2] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line1[2] == grid_line2[4] && grid_line2[4] == grid_line3[6]) {
        if (grid_line1[2] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line1[2] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line1[2] == grid_line2[2] && grid_line2[2] == grid_line3[2]) {
        if (grid_line1[2] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line1[2] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line1[4] == grid_line2[4] && grid_line2[4] == grid_line3[4]) {
        if (grid_line1[4] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line1[4] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line2[2] == grid_line2[4] && grid_line2[4] == grid_line2[6]) {
        if (grid_line2[2] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line2[2] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line3[2] == grid_line3[4] && grid_line3[4] == grid_line3[6]) {
        if (grid_line3[2] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line3[2] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line3[2] == grid_line2[4] && grid_line2[4] == grid_line1[6]) {
        if (grid_line3[2] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line3[2] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } else if (grid_line1[6] == grid_line2[6] && grid_line2[6] == grid_line3[6]) {
        if (grid_line1[6] == p1_piece) {
            std::cout << "Player 1 wins!\n";
            winner = true;
        } else if (grid_line1[6] == p2_piece) {
            std::cout << "Player 2 wins!\n";
            winner = true;
        }
    } 
}

void play_again() {
    
    std::string response = "";
    while (response != "y" && response != "n"){
        std::cout << "Would you like to play again? y/n\n";
        std::cin >> response;
    }
    if (response == "y") {
        grid_line0 = {" " ," ", "a", " ", "b", " ", "c"};
        grid_line1 = {"1" ," ", "_", "|", "_", "|", "_"};
        grid_line2 = {"2" ," ", "_", "|", "_", "|", "_"};
        grid_line3 = {"3" ," ", " ", "|", " ", "|", " "};
        p1_on = false;
        p2_on = false;
        winner = false;
    } else if (response == "n") {
        std::cout << "Thank you for playing Tic Tac Toe!";
        play = false;
    } else {
        std::cout << "Sorry, I didn't catch that.\n";
    }
}

void play_game() {

    int turns = 0;
    turns = 0;
    while (winner == false && turns < 9){
        grid();
        player_1();
        win_condition();
        turns++;
        if (winner == true || turns == 9){
            grid();
            break;
        }
        grid();
        player_2();
        win_condition();
        turns++;
        if (winner == true || turns == 9){
            grid();
            break;
        }

    }
    if (turns == 9){
        std::cout << "It's a draw!\n";
    }
    play_again();
}


int main() {

    while (play == true) {
        play_game();
    }

}