#include <chrono>
#include <iostream>
#include <thread>

// Define the decorator equivalent
template <typename Func>
auto execution_time(Func func) {
    return [func]() {
        // Record the start time
        auto start_time = std::chrono::high_resolution_clock::now();

        // Call the original function
        auto result = func();

        // Record the end time
        auto end_time = std::chrono::high_resolution_clock::now();

        // Calculate execution time
        auto duration =
            std::chrono::duration<double>(end_time - start_time).count();
        std::cout << "Function executed in " << duration << " seconds"
                  << std::endl;

        return result;
    };
}

// Define a function to simulate slow operation
std::string slow_function() {
    std::this_thread::sleep_for(
        std::chrono::seconds(2));  // Simulate a slow operation
    return "Finished";
}

int main() {
    // Use the decorator equivalent
    auto decorated_function = execution_time(slow_function);

    // Call the decorated function
    std::cout << decorated_function() << std::endl;

    return 0;
}
