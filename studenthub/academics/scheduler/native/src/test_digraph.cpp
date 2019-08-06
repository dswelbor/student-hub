/**
 * Simple test driver for generic (template) digraph library
 *
 * @author David Welborn
 * @version 08.05.2019
 */
#include "catch/catch.hpp" // Unit testing framework
#include "digraph.h"
#include "digraph.cpp"
#include <string>


/**
 * Test addVertex() works as intended
 */
TEST_CASE( "TestCase1: addVertex() adds vertices to digraph", "[digraph]" ) {


    DiGraphOrdered<int> testINT;
    std::vector<int> testINTVector;

    // Empty digraph
    REQUIRE(testINT.size() == 0);
    REQUIRE(*(testINT.getVertices()) == testINTVector);

    testINT.addVertex(40);
    testINT.addVertex(39);
    testINT.addVertex(39); // non-unique vertex, should not be added
    testINT.addVertex(41);

    // Populate vector with expected vertices and ordering
    testINTVector.push_back(39);
    testINTVector.push_back(40);
    testINTVector.push_back(41);

    // size and contents are equivalent
    REQUIRE(testINT.size() == 3);
    REQUIRE(*(testINT.getVertices()) == testINTVector);
}

/**
 * Test addEdge() to add unique directed edges as needed and add vertices if not
 * already present in graph.
 */
TEST_CASE("TestCase2: addEdge() updates adjList and adds vertices on demand") {
    DiGraphOrdered<int> testINT;

    testINT.addVertex(40);
    testINT.addVertex(39);
    testINT.addVertex(41);

    // 3 vertices, no edges
    REQUIRE(testINT.getAdj(40)->empty());
    REQUIRE(testINT.getAdj(39)->empty());
    REQUIRE(testINT.getAdj(41)->empty());

    testINT.addEdge(38,47); // 38 -> 47
    testINT.addEdge(38,39); // 38 -> 49
    testINT.addEdge(38,42); // 38 -> 42
    testINT.addEdge(38,47); // 38 -> 47 non-unique, should not be added
    testINT.addEdge(40,42); // 40 -> 42

    // Graph now has 6 edges
    std::vector<int> testINTVector = {38, 39, 40, 41, 42, 47};
    REQUIRE(testINT.size() == 6);
    REQUIRE(*(testINT.getVertices()) == testINTVector);

    // 3 Edges added from 38 and 1 from 40
    REQUIRE(testINT.getAdj(38)->size() == 3);
    REQUIRE(testINT.getAdj(40)->size() == 1);

    // directed edges from 38 -> 47, 49, 42 & 40 -> 42
    std::vector<int> testAdj38 = {47, 39, 42};
    std::vector<int> testAdj40 = {42};
    REQUIRE(*(testINT.getAdj(38)) == testAdj38);
    REQUIRE(*(testINT.getAdj(40)) == testAdj40);

    // Vertices 39, 41, 42, 47 still have outdegree 0
    REQUIRE(testINT.getAdj(39)->empty());
    REQUIRE(testINT.getAdj(41)->empty());
    REQUIRE(testINT.getAdj(41)->empty());
    REQUIRE(testINT.getAdj(47)->empty());
}

/**
 * Tests removeVertex() to ensure correct vertex is removed from digraph,
 * vertex is removed from all adjacency lists, digraph size is updated correctly,
 * and remaining vertices remain intact.
 */
TEST_CASE("TestCase3: removeVertex() effectively removes vertex") {
    // build digraph
    DiGraphOrdered<int> testINT;
    testINT.addVertex(1);
    testINT.addVertex(2);
    testINT.addVertex(3);
    testINT.addEdge(4,3); // 4 -> 3
    testINT.addEdge(5,3); // 5 -> 3
    testINT.addEdge(6,4); // 6 -> 4
    testINT.addEdge(3,1); // 3 -> 1

    // Graph has 6 vertices
    std::vector<int> testINTVector = {1, 2, 3, 4, 5, 6};
    REQUIRE(testINT.size() == 6);
    REQUIRE(*(testINT.getVertices()) == testINTVector);
    // 3, 4, 5, 6 have outdegree 1
    REQUIRE(testINT.getAdj(3)->size() == 1);
    REQUIRE(testINT.getAdj(4)->size() == 1);
    REQUIRE(testINT.getAdj(5)->size() == 1);
    REQUIRE(testINT.getAdj(6)->size() == 1);
    // directed edges from 3->1, 4->3, 5->3, 6->4
    std::vector<int> testAdj3 = {1};
    std::vector<int> testAdj4 = {3};
    std::vector<int> testAdj5 = {3};
    std::vector<int> testAdj6 = {4};
    REQUIRE(*(testINT.getAdj(3)) == testAdj3);
    REQUIRE(*(testINT.getAdj(4)) == testAdj4);
    REQUIRE(*(testINT.getAdj(5)) == testAdj5);
    REQUIRE(*(testINT.getAdj(6)) == testAdj6);
    // Vertices 1 and 2 have outdegree = 0
    REQUIRE(testINT.getAdj(1)->empty());
    REQUIRE(testINT.getAdj(2)->empty());

    // delete vertex 3
    testINT.removeVertex(3);

    // digraph has 5 vertices
    std::vector<int> testINTVectorAfter = {1, 2, 4, 5, 6};
    REQUIRE(testINT.size() == 5);
    REQUIRE(*(testINT.getVertices()) == testINTVectorAfter);
    // directed edges from->to: 6->4, outdegree = 1
    REQUIRE(testINT.getAdj(6)->size() == 1);
    REQUIRE(*(testINT.getAdj(6)) == testAdj6);
    // Vertices 1, 2, 4, and 5 have outdegree = 0
    REQUIRE(testINT.getAdj(1)->empty());
    REQUIRE(testINT.getAdj(2)->empty());
    REQUIRE(testINT.getAdj(4)->empty());
    REQUIRE(testINT.getAdj(5)->empty());
    // Adjacency list for vertex 3 (deleted) == null
    REQUIRE(testINT.getAdj(3) == NULL);
}

/**
 * Verify that getAdj() returns a ptr to an acurate representative adjacency
 * list, empty but non-null vectors for vertices with outdegree = 0, and NULL
 * for vertices not present in digraph
 */
TEST_CASE("TestCase4: getAdj() returns a vector ptr representing adj list") {
    // Set-up graph
    DiGraphOrdered<std::string> testDiGraph;
    testDiGraph.addEdge("nodeA", "nodeB"); // nodeA->nodeB
    testDiGraph.addEdge("nodeB", "nodeC"); // nodeB->nodeC, nodeC->{}
    testDiGraph.addVertex("nodeD"); // nodeD->{}

    std::vector<std::string> testA = {"nodeB"};
    std::vector<std::string> testB = {"nodeC"};
    std::vector<std::string> testC;
    std::vector<std::string> testD;

    // NodeA points to "nodeB"
    REQUIRE(*(testDiGraph.getAdj("nodeA")) == testA);
    // NodeB points to "nodeC"
    REQUIRE(*(testDiGraph.getAdj("nodeB")) == testB);
    // NodeC and NodeD point to nothing
    REQUIRE(*(testDiGraph.getAdj("nodeC")) == testC);
    REQUIRE(*(testDiGraph.getAdj("nodeD")) == testD);
    REQUIRE(testDiGraph.getAdj("nodeC")->empty());
    REQUIRE(testDiGraph.getAdj("nodeD")->empty());
    // NodeE dne and should have a null adjList
    REQUIRE(testDiGraph.getAdj("nodeE") == NULL);
}

/**
 * Verify getVertices returns a vector ptr that accurately represents current
 * state of the digraph
 */
TEST_CASE("TestCase5: getVertices() returns an accurate vector<Vertex>") {
    // Generate graph
    DiGraphOrdered<int> testDiGraph;
    testDiGraph.addVertex(1);
    testDiGraph.addVertex(3);
    testDiGraph.addVertex(5);
    testDiGraph.addVertex(4);
    std::vector<int> vectorBefore = {1, 3, 4, 5};

    // Graph has correct vertices and size = 4
    REQUIRE(testDiGraph.getVertices()->size() == 4);
    REQUIRE(*(testDiGraph.getVertices()) == vectorBefore);

    // Add new values
    testDiGraph.addVertex(-3);
    testDiGraph.addVertex(127);

    // Graph has correct vertices and size = 6
    std::vector<int> vectorAfter = {-3, 1, 3, 4, 5, 127};
    REQUIRE(testDiGraph.getVertices()->size() == 6);
    REQUIRE(*(testDiGraph.getVertices()) == vectorAfter);


}

/**
 * Verify getIndegree() calculates the accurate inDegree value for a given
 * vertex in the graph.
 */
TEST_CASE("TestCase6: getIndegree() returns the correct inDegree value") {
    // Setup graph
    DiGraphOrdered<int> testGraph;
    testGraph.addEdge(1,3); // 1->3
    testGraph.addEdge(2, 3); // 2->3
    testGraph.addEdge(4, 1);
    testGraph.addVertex(5);

    // graph contains {1, 2, 3, 4, 5} and size = 5
    std::vector<int> testV = {1, 2, 3, 4, 5};
    REQUIRE(testGraph.size() == 5);
    REQUIRE(*(testGraph.getVertices()) == testV);

    // vertex 1 has indegree 1
    REQUIRE(testGraph.getInDegree(1) == 1);
    // vertex 2 has indegree 0
    REQUIRE(testGraph.getInDegree(2) == 0);
    // vertex 3 has indegree = 2
    REQUIRE(testGraph.getInDegree(3) == 2);
    // vertex 4 has indegree = 0
    REQUIRE(testGraph.getInDegree(4) == 0);
    // vertex 5 has indegree = 0
    REQUIRE(testGraph.getInDegree(5) == 0);

}


TEST_CASE("TestCase7: size() returns an accurate size for the graph") {
    // build digraph
    DiGraphOrdered<int> testINT;

    // Graph should be empty
    REQUIRE(testINT.size() == 0);

    // Add 3 vertices
    testINT.addVertex(1);
    testINT.addVertex(2);
    testINT.addVertex(3);

    // Graph should have size = 3
    REQUIRE(testINT.size() == 3);

    // Remove 2 vertices
    testINT.removeVertex(2);
    testINT.removeVertex(1);

    // Graph should have size = 1
    REQUIRE(testINT.size() == 1);

    // Remove 2 vertices
    testINT.removeVertex(3);
    testINT.removeVertex(4); // not present in graph

    // Graph should have size = 0
    REQUIRE(testINT.size() == 0);

}
/*SECTION( "resizing bigger changes size and capacity" ) {
v.resize( 10 );

REQUIRE( v.size() == 10 );
REQUIRE( v.capacity() >= 10 );
}
SECTION( "resizing smaller changes size but not capacity" ) {
v.resize( 0 );

REQUIRE( v.size() == 0 );
REQUIRE( v.capacity() >= 5 );
}
SECTION( "reserving bigger changes capacity but not size" ) {
v.reserve( 10 );

REQUIRE( v.size() == 5 );
REQUIRE( v.capacity() >= 10 );
}
SECTION( "reserving smaller does not change size or capacity" ) {
v.reserve( 0 );

REQUIRE( v.size() == 5 );
REQUIRE( v.capacity() >= 5 );
}
}*/