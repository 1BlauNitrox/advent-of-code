#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

//Part 1
int compare_lists_by_distance(std::vector<int> list1, std::vector<int> list2) {
    std::sort(list1.begin(), list1.end());
    std::sort(list2.begin(), list2.end());

    if (list1.size() != list2.size()) {
        return 0;
    }
    long result = 0;
    for (int i = 0; i < list1.size(); i++) {
        result += abs(list1[i] - list2[i]);
    }
    return result;
}

//Part 2
int compare_lists_by_duplicates(std::vector<int> list1, std::vector<int> list2) {
    if (list1.size() != list2.size()) {
        return 0;
    }
    long result = 0;


    for (int i = 0; i < list1.size(); i++) {
        int duplicates = 0;
        for(int j = 0; j < list1.size(); j++) {
            if(list1[i] == list2[j]) {
                duplicates++;
            }
        }
        result += list1[i] * duplicates;
    }


    return result;
}

int main(int argc, char const *argv[]) {
    std::string filename = "input.txt";

    // Vektoren für linke und rechte Zahlen
    std::vector<int> left_values;
    std::vector<int> right_values;

    // Datei öffnen
    std::ifstream infile(filename);

    if (!infile) {
        std::cerr << "Fehler beim Öffnen der Datei " << filename << std::endl;
        return 1;
    }

    int left, right;

    // Zeilenweise Einlesen
    while (infile >> left >> right) {
        left_values.push_back(left);
        right_values.push_back(right);
    }

    infile.close();

    std::cout << compare_lists_by_distance(left_values, right_values) << std::endl;
    std::cout << compare_lists_by_duplicates(left_values, right_values) << std::endl;

    return 0;
}
