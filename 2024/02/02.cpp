#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

int collect_save_reports(std::vector<std::vector<int>> reports) {
    int save_reports = 0;
    for(auto report : reports) {
        bool save_report = true;
        bool increasing;
        int last;

        for(size_t i = 0; i < report.size(); i++) {
            if(i == 0) {
                last = report[i];
                continue;
            }

            if(i == 1) {
                increasing = report[i] > last;
            }

            if((increasing && report[i] <= last) || (!increasing && report[i] >= last)) {
                save_report = false;
                break;
            }

            int diff = abs(report[i] - last);
            if(!(diff <= 3 && diff >= 1)) {
                save_report = false;
                break;
            }
            

            last = report[i];
        }
        if(save_report) {
            save_reports++;
        } 
    }
    return save_reports;
}


int main() {
    std::ifstream inputFile("input.txt"); // Datei öffnen
    if (!inputFile) {
        std::cerr << "Fehler beim Öffnen der Datei!" << std::endl;
        return 1;
    }

    std::vector<std::vector<int>> reports; // Vektor von Vektoren

    std::string line;
    while (std::getline(inputFile, line)) { // Zeile für Zeile lesen
        std::istringstream iss(line);
        std::vector<int> report;
        int number;

        // Zahlen aus der aktuellen Zeile extrahieren und in den Vektor schreiben
        while (iss >> number) {
            report.push_back(number);
        }

        // Den aktuellen Vektor zur Sammlung hinzufügen
        reports.push_back(report);
    }

    inputFile.close(); // Datei schließen

    std::cout << collect_save_reports(reports) << std::endl;

    return 0;
}
