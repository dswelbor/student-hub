#ifndef NATIVE_COURSE_H
#define NATIVE_COURSE_H

#include <string>
#include <forward_list>
/**
 * Class to wrap course information including department and course number identifiers,
 * credit hours, pre/co - requisites, and a textual description
 *
 * @author David Seth Welborn
 * @version 08.07.2019
 */
class Course {
private:
    // Basic course atttributes
    std::string department;
    int courseNo;
    int credits;
    std::string description;

    // course relations
    std::forward_list<Course*> prereqs;
    std::forward_list<Course*> coreqs;

    // List clones
    std::forward_list<Course*> prereqsClone;
    std::forward_list<Course*> coreqsClone;

    /**
     * Helper method that inserts unique Course ptr elements to a list of Course
     * ptrs. Returns boolean success value.
     * @param thisList ptr to target list
     * @param element ptr to Course element insertion candidate
     * @return true if successfully added, false otherwise
     */
    bool addToListSorted(std::forward_list<Course*>* thisList, Course* element);

    /**
     * Helper method that removes Course ptr elements from a sorted list of
     * unique Course ptrs.
     * @param thisList ptr to target list
     * @param element ptr to Course element removal candidate
     * @return true successfully removed, false otherwise
     */
    //bool remFromListSorted(std::forward_list<Course*>* thisList, Course* element);

public:
    /**
     * Constructor - makes a new Course object with department, course number,
     * and credit hour data. Defaults to blank description, and empty prereq and
     * coreq vectors.
     * @param dept ptr to department string
     * @param no Course number
     * @param credits number of credits for Course
     */
    Course(std::string* dept, int no, int credits);

    /**
     * Accessor function that gets the course identifier composed of department
     * string and course number.
     * @return unique course identifier
     */
    std::string getCourseID() const;

    /**
     * Simple mutator function that sets the description text for a Course
     * @param descr ptr to Course string description
     */
    void setDescription(std::string* descr);

    /**
     * Adds another course as a pre-requisite for taking this course
     * @param course pre-requisite
     */
    void addPrereq(Course* course);

    /**
     * Adds a course co-requisite relationship
     * @param course co-requisite for this course
     */
    void addCoreq(Course* course);

    /**
     * Removes a pre-requisite for this course if it exists
     * @param course ptr tp pre-requisite to be removed
     */
    void removePrereq(Course* course);

    /**
     * Removes a course co-requisite relationship if it exists
     * @param course ptr to co-requisite to be removed
     */
    void removeCoreq(Course* course);

    /**
     * Accessor function that returns the pre-requisites for this course
     * @return pre-requisites for the Course
     */
    std::forward_list<Course*>* getPrereqs();

    /**
     * Accessor function that returns the co-requites for this course
     * @return co-requisites for the Course
     */
    std::forward_list<Course*>* getCoreqs();

    /**
     * Destructor definition
     */
    virtual ~Course();

    /**
     * Overide the < operator function
     * @return
     */
    friend bool operator < (const Course&, const Course&);

};



#endif //NATIVE_COURSE_H
