//This is a testing framework for slave programs
//Include the slave program here and let the compute function run from main
#include "hello.hpp"

#include <iostream>

using namespace std;

int main(int argv, char * argc[]){
    cout << "Initiating runner..." << endl;

    int lval = 5;
    int res = compute(lval);

    cout << "Runner output:" << endl << res << endl;

    cout << "done." << endl;
}