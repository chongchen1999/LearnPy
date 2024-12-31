#include <functional>
#include <iostream>

std::function<int(int)> test(int number) {
    return [number](int number_in) -> int { return number_in + number; };
}

int main() {
    auto ret = test(5);
    std::cout << typeid(ret).name() << std::endl;

    // Print the function object address (simulates Python's function object
    // output).
    std::cout << "Function object created\n";

    std::cout << ret(10) << std::endl;  // Equivalent to ret(10) in Python
    std::cout << ret(20) << std::endl;  // Equivalent to ret(20) in Python

    return 0;
}
