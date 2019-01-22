//#include "stdafx.h"
#include "fstream"
#include "iostream"
#include "thread" // <-- Чтобы распараллелить
#include "string"
#include <cstdlib>

const double min_T = 0.4;
const double max_T = 1.1;

const double min_p = 0.0001;
const double max_p = 0.11;

const double step_T = 0.1;
const double step_p = 0.0002;


int create(double p){
    std::string command = "lmp_serial < in.lennardjonescrystal -var pressure " + std::to_string(p);
    std::system(command.c_str());
    for (double T = min_T; T < max_T; T = T + step_T)
    {
        command = "lmp_serial < in.restart -var temperature " + std::to_string(T) + " -var pressure " + std::to_string(p);
        std::system(command.c_str());
        //std::cout << command << std::endl;
    }
    return 0;
}

int main(){
    std::ios_base::sync_with_stdio(false);
    for (double p = min_p; p < max_p; p = p + 4*step_p) // так как у меня 4 процессора
    {
        std::thread P1(create, p);
        std::thread P2(create, p + step_p);
        std::thread P3(create, p + 2*step_p);
        std::thread P4(create, p + 3*step_p);
        
        P1.join();
	    P2.join();
	    P3.join();
	    P4.join();
        //std::cout << p << std::endl;
    }

    return 0;
}