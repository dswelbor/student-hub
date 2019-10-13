#ifndef DIGRAPH_H
#define DIGRAPH_H

#include <map>
//#include <list>
#include <vector>
template <typename Vertex>

/**
 * Digraph class header. Declares the member variables and functions for a
 * directed graph structured as an ordered map. This speeds up functions that
 * iterate over all vertices in the graph.
 * @tparam Vertex
 *
 * @author David Welborn
 * @version 08.04.2019
 */
class DiGraphOrdered {
private:
    // Hashmap internal representation of directed graph
    std::map<Vertex, std::vector<Vertex>> vertices;
    // Allocated for list of graph vertices
    std::vector<Vertex> vertexList;
    // Allocate for list of "adjacent" vertices
    std::vector<Vertex> adjList;
    // Number of vertices in digraph
    int count;

public:
    /**
     * Default constructor
     */
    DiGraphOrdered();

    /**
     * Adds an edge from one vertex to another. If Vertex is not present, the function
     * adds it to the graph. Duplicate vertices and edges are disallowed
     * @param from vertex the edge originates from
     * @param to vertex pointed to
     */
    void addEdge(Vertex from, Vertex to);

    /**
     * Adds a vertex to directed graph is not already present
     * @param newVertex
     */
    void addVertex(Vertex newVertex);

    /**
     * Removes a vertex from the graph and all edges referencing it
     * @param vertex to be deleted
     */
    void removeVertex(Vertex vertex);

    /**
     * Returns the a pointer to the adjacency list for the passed vertex.
     * @param vertex
     * @return vertex adjacency list
     */
    std::vector<Vertex>* getAdj(Vertex vertex);

    /**
     * Get a linked list of all vertices present in graph
     * @return list of vertices
     */
    std::vector<Vertex>* getVertices();

    /**
     * Gets the indegree value of a specified vertext
     * @param vertex
     * @return indegree value
     */
    int getInDegree(Vertex vertex);

    /**
     * Gets the number of vertices present in digraph
     * @return
     */
    int size();

    /**
     * Destructor to de-allocate memory used by DiGraph object
     */
    virtual ~DiGraphOrdered();
};

#endif