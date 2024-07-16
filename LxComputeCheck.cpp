#include <iostream>
#include <fstream>
#include <chrono>
#include <thread>
 
// Function to read CPU usage from /proc/stat
double ComputeCheck() {
    std::ifstream statFile("/proc/stat"); \
    std::string line;

    // Read the first line
    std::getline(statFile, line); 
 
    // Extract CPU usage values
    long user, nice, system, idle, iowait, irq, softirq;
    sscanf(line.c_str(), "cpu %ld %ld %ld %ld %ld %ld %ld", &user, &nice, &system, &idle, &iowait, &irq, &softirq);
 
    // Calculate total time spent by CPU
    long total = user + nice + system + idle + iowait + irq + softirq;
 
    // Calculate usage percentage
    double usage = 100.0 * (1.0 - static_cast<double>(idle) / total);
    return usage;
}
 
int main() {
    while (true) {
        double ComputeUsage = ComputeCheck();
        std::cout << "CPU Usage: " << ComputeUsage << "%" << std::endl;
 
        // Sleep for 1 second
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
 
    return 0;
}
