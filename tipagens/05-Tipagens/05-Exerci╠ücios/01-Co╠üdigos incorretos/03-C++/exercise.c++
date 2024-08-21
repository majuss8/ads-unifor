#include <iostream>
#include <string>

void printDetails(const std::string& name, int age) {
    std::cout << "Name: " << name << ", Age: " << age << std::endl;
}

int main() {
    std::string name = "John";
    int age;
    age = 25; // inicializando a variável com um valor válido

    printDetails(name, age);

    // Correção do uso de ponteiros
    int* ptr = new int;  // Alocando memória dinamicamente
    *ptr = 100;          // Atribuindo valor à memória alocada
    std::cout << *ptr << std::endl;

    delete ptr;  // Liberando a memória alocada

    return 0;
}
