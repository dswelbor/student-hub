#ifndef NATIVE_MAJOR_H
#define NATIVE_MAJOR_H

#include <string>
#include "course.h"
#include "digraph.h"
/**
 * A class that encapsulates the course requirements for a Major
 */

class Major {
private:
    std::string name;
    DiGraphOrdered<Course> courses;
    int size;

};


#endif //NATIVE_MAJOR_H
