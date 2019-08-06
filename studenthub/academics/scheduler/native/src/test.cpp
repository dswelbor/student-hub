/**
 * Simple test driver for unit tests
 *
 * @author David Welborn
 * @version 08.05.2019
 */

#define CATCH_CONFIG_MAIN  // Provides main()
#include "catch/catch.hpp" // Unit testing framework
// '#include' additional test cases



// TODO: Refactor with proper unit tests
/*
#include <iostream>
#include "digraph.h"
#include "digraph.cpp"
int main() {
    DiGraphOrdered<int> testINT;

    testINT.addVertex(40);
    testINT.addVertex(39);
    testINT.addEdge(38,47);
    testINT.addEdge(38,39);
    testINT.addEdge(38,42);
    testINT.addEdge(40,42);
    auto *vert = testINT.getVertices();
    for (int i = 0; i < vert->size(); i++) {
        std::cout << (*vert)[i] << " ";
    }
    testINT.removeVertex(39);
    auto* result = testINT.getAdj(38);
    std::cout << "\n" << (*result).size() << "\n";
    auto* result2 = testINT.getAdj(40);
    std::cout << (*result2).size() << "\n";

    vert = testINT.getVertices();
    for (int i = 0; i < vert->size(); i++) {
        std::cout << (*vert)[i] << " \n";
    }

    // Test indegree function
    std::cout << testINT.getInDegree(40) << ": Expect 0\n";
    std::cout << testINT.getInDegree(47) << ": expect 1\n";
    std::cout << testINT.getInDegree(42) << ": expect 2\n";
    std::cout << testINT.getInDegree(38) << ": expect 0\n";


    return 0;

}
 */