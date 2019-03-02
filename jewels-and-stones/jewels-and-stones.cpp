#include <string>
#include <ostream>
#include <iostream>

int numJewelsInStones (std::string J, std::string S){
    std::cout<< " J: " << J << "S: " << S << std::endl;
    int jewelcount = 0;
    for ( int jiter = 0 ; jiter < J.length(); jiter++){
        for (int siter = 0; siter < S.length(); siter++){
            if (J.c_str()[jiter] == S.c_str()[siter]){
                jewelcount++;
            }
        }
        
    }
    return jewelcount;
}

int main(){
    //J = "aA", S = "aAAbbbb" should output 3
    std::cout << numJewelsInStones( "aA" , "aAAbbbb" ) << std::endl;
    //J = "z" S= "ZZ" should output 0
    std::cout << numJewelsInStones( "z" , "ZZ" ) << std::endl;
}