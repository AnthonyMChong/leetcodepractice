#include <string>
#include <ostream>
#include <iostream>

std::string toLowerCase (std::string str){
    std::string returnString = "";
    //strarray char [str.length()];
    for (int strIndex = 0; strIndex < str.length() ; strIndex++){
        returnString += tolower(str.c_str()[strIndex]) ;
    }

    return returnString;
}

int main(){
    std::cout<< toLowerCase("HeLlo WORld") << std::endl;
    std::cout<< toLowerCase("LOVELY") << std::endl;

}