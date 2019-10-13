/**
 * Implementation for Course class wrapping information including department
 * and course number identifiers, credit hours, pre/co - requisites, and a
 * textual description
 *
 * @author David Seth Welborn
 * @version 08.08.2019
 */
#include "Course.h"

/**
 * Course constructor implementation. Accepts a department abbreviation string,
 * a course number, and the number of credit hours for a given Course.
 * @param dept ptr to department abbreviation string
 * @param no Course number
 * @param credits number of credit hours
 */
Course::Course(std::string* dept, int no, int credits) {
    // TODO: implement with a thread-safe shared pointer
    this->department = *dept;
    this->courseNo = no;
    this->credits = credits;
    // Rely on RAII for pre-req and co-req Course vectors
}

/**
 * Concatenates department abbreviation and course number to generate a "unique"
 * course identifier.
 * @return unique Course identifier string
 */
std::string Course::getCourseID() const {
    return this->department + std::to_string(this->courseNo);
}

/**
 * Sets the Course descriptive text. Replaces any existing Course descriptive text.
 * @param descr ptr to Course descriptive string
 */
void Course::setDescription(std::string* descr) {
    this->description = *descr;
}

/**
 * Adds passed Course to the Course's list of pre-requisites.
 * @param course ptr to Course pre-req to add
 */
void Course::addPrereq(Course* course) {
    this->addToListSorted(&(this->prereqs), course);
}

/**
 * Adds passed Course ptr to Course's list of co-requisites.
 * @param course ptr to Course co-req for insertion
 */
void Course::addCoreq(Course* course) {
    this->addToListSorted(&(this->coreqs), course);
}


/**
 * Removes a course pre-requisite relationship if it exists
 * @param course ptr to pre-requisite to be removed
 */
void Course::removePrereq(Course* course) {
    this->prereqs.remove(course);
}

/**
 * Removes a course co-requisite relationship if it exists
 * @param course ptr to co-requisite to be removed
 */
void Course::removeCoreq(Course* course) {
    // TODO: Implement this
    this->coreqs.remove(course);
}

/**
 * Accessor function that returns the pre-requisites for this course
 * @return pre-requisites for the Course
 */
std::forward_list<Course*>* Course::getPrereqs() {
    this->prereqsClone = this->prereqs;
    return &(this->prereqsClone);
}

/**
 * Accessor function that returns the co-requites for this course
 * @return co-requisites for the Course
 */
std::forward_list<Course*>* Course::getCoreqs() {
    this->coreqsClone = this->coreqs;
    return &(this->coreqsClone);

}

/**
 * Simple function defines (overrides) < operator functionality for Course
 * objects.
 * @param courseA 'lesser' Course object
 * @param courseB  'greater' Course object
 * @return true if courseA ID < courseB, false otherwise
 */
bool operator < ( const Course& courseA, const Course& courseB) {
    return courseA.getCourseID() < courseB.getCourseID();
}

/**
 * Simple helper function that adds unique Course elements ptrs to Courses'
 * self-referential lists of Courses.
 * @param thisList ptr to List of Course ptrs
 * @param element Course ptr to insertion element
 * @return true if element added, false if otherwise
 */
bool Course::addToListSorted(std::forward_list<Course *> *thisList,
                             Course *element) {
    // Empty list OR element < list head
    if (thisList->empty() || *element < **(thisList->begin())) {
        thisList->push_front(element); // add element ptr to head
        return true;
    }
        // Iterate through remainder of list
    else {
        auto it = thisList->begin();
        auto next = ++(thisList->begin());
        bool added = false;
        while (!added) {
            // Element not unique
            if (element->getCourseID() == (*it)->getCourseID()) {
                return false;
            }
                // End of list or passed element < next element
            else if (next == thisList->end() || *element < **next) {
                thisList->insert_after(it, element);
                added = true;
            }
                // passed element > next element
            else {
                // increment iterators
                ++it;
                ++next;
            }
        }

        // element was added
        return true;
    }
}

/**
     * Helper method that removes Course ptr elements from a sorted list of
     * unique Course ptrs. Assumes each element is unique and list is sorted.
     * @param thisList ptr to target list
     * @param element ptr to Course element removal candidate
     * @return true successfully removed, false otherwise
     */
     /*
bool remFromListSorted(std::forward_list<Course*>* thisList, Course* element) {
    // Special case - list is empty
    if (thisList->empty()) {
        return false;
    }
    // List is not empty
    else {
        // iterate through elements
        auto it = thisList->begin();
        //auto next = ++(thisList->begin());
        while (it != thisList->end()) {
            // TODO: Iterate through elements and remove candidate
            // Element not present - current element > passed element
            if (*element < **it) {
                return false; // Nothing removed
            }
            // Element found
            else if (element->getCourseID() == (*it)->getCourseID()) {
                thisList->remove()
            }
            // if...
            // remove...
            removed = true;
            // return true
            // else
            // increment iterators
        }

        // Not removed
        return false;
    }
}
      */

/**
 * Destructor default implementation frees memory allocated for Course
 * attributes
 */
Course::~Course() = default;


