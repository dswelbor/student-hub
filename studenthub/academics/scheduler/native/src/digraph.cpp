#ifndef DIGRAPH_CPP
#define DIGRAPH_CPP

#include "digraph.h"
#include <map>
#include <iostream>

/**
 * Provides implementation for the digraph.h header file, implementing the
 * generic (templated) directed graph functions.
 *
 * @author David Welborn
 * @version 08.04.2019
 */

/**
 * Default ctor - follows RAII (Resource Allocation in Initialization)
 * @tparam Vertex
 */
template <typename Vertex>
DiGraphOrdered<Vertex>::DiGraphOrdered() {
    // Initialize digraph with size 0
    // vertices map will allocate in initialization (first vertex)
    this->size = 0;
}

/**
 * Adds a directed edge from one vertex to another. If the vertex is not present,
 * it adds the vertex to the graph
 * @tparam Vertex template
 * @param from Vertex
 * @param to Vertex
 */
template <typename Vertex>
void DiGraphOrdered<Vertex>::addEdge(Vertex from, Vertex to) {
    // from vertex not in graph
    if (0 == this->vertices.count(from)) {
        this->addVertex(from);
    }
    // to vertex not in graph
    if (0 == this->vertices.count(to)) {
        this->addVertex(to);
    }

    // Add directed edge to
    // TODO: Insert sorted
    this->vertices[from].push_back(to);
}

/**
 * Function adds a passed vertex to the directed graph. If Vertex is aready
 * present, function does nothing.
 * @tparam Vertex  template
 * @param newVertex add to graph
 */
template <typename Vertex>
void DiGraphOrdered<Vertex>::addVertex(Vertex newVertex) {
    // vertex not present
    if (!this->vertices.count(newVertex)) {
        this->vertices.insert({newVertex, std::vector<Vertex>()});
        this->size++;
    }
}

/**
 * Removes vertex from graph and all directed edges that point to it
 * @tparam Vertex template
 * @param vertex to be removed
 */
template <typename Vertex>
void DiGraphOrdered<Vertex>::removeVertex(Vertex vertex) {
    // TODO: erase using iterator to improve efficiency
    // vertex present
    if (this->vertices.count(vertex)) {
        this->vertices.erase(vertex);
        this->size--;

        // TODO: Remove from adjacency lists
    }
}

/**
 * Returns a pointer to the adjacency list vector for the passed vertex
 * @tparam Vertex template
 * @param vertex target
 * @return adjacency list (vector) pointer
 */
template <typename Vertex>
std::vector<Vertex>* DiGraphOrdered<Vertex>::getAdj(Vertex vertex) {
    // TODO: Implement this
    // TODO: Implement with iterator for faster performance
    // vertex present
    if (this->vertices.count(vertex) > 0) {
        // adjacency list is value in mapped key:value pair
        // Erase previous adj list
        //this->adjList.erase (adjList.begin(),adjList.end());
        this->adjList = this->vertices[vertex];
        return &(this->adjList);
        //return &(this->vertices[vertex]);
    }
    // vertex not present
    else {
        return NULL;
    }
}

/**
 * Gets all vertices in a directed graph and returns a pointer to a vector
 * containing all vertices.
 * @tparam Vertex template
 * @return pointer to vector with all vertices
 */
template <typename Vertex>
std::vector<Vertex>* DiGraphOrdered<Vertex>::getVertices() {
    // Erase vertexList
    this->vertexList.erase(vertexList.begin(), vertexList.end());
    // Populate vertices

    auto it = this->vertices.begin();
    for (int i = 0; i < this->size; i++) {
        this->vertexList.push_back((it++)->first);

    }
    // Return a pointer to vertices vector list
    return &(this->vertexList);
}

/**
 * Returns the in-degree value for a given vertex. Note: Also return 0 for
 * vertices not present in graph
 * @tparam Vertex template
 * @param vertex target
 * @return in-degree non-negative int value
 */
template <typename Vertex>
int DiGraphOrdered<Vertex>::getInDegree(Vertex vertex) {
    int inDegree = 0; // initialize indegree as 0
    // Iterate through each vertex adjacency list
    for (auto it = this->vertices.begin(); it != this->vertices.end(); ++it) {
        // Iterate down each list
        for (auto itList = it->second.begin(); itList != it->second.end(); ++itList) {
            if (*itList == vertex) {
                ++inDegree;
            }
        }
    }
    // return inDegree
    return inDegree;
}

/**
 * Destructor to de-allocate memory used by DiGraph object
 */
template <typename Vertex>
DiGraphOrdered<Vertex>::~DiGraphOrdered() {
    // TODO: Implement as required for RAII elements
}

#endif