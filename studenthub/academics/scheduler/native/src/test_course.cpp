#include "catch/catch.hpp" // Unit testing framework
#include "Course.h"
//#include <string>

/**
* Simple test driver for Course class
*
* @author David Welborn
* @version 08.12.2019
*/


/**
 * Verifies < operator properly overridden
 */
TEST_CASE("CourseTestCase1: Course < operator overriden") {
    std::string smallSTR = "BIO";
    std::string bigSTR = "MAT";
    Course testSmall = Course(&smallSTR, 123, 3);
    Course testBig = Course(&bigSTR, 234, 3);

    REQUIRE(testSmall < testBig); // small < big == true
    REQUIRE(!(testBig < testSmall)); // big < small == false
    REQUIRE(!(testSmall < testSmall)); // small < small == false

    // TODO: Add more edge cases
}

/**
 * Verifies getCcourseID() returns the correct string Course ID
 */
TEST_CASE("CourseTestCase2: getCourseID returns correct string") {
    std::string math = "MAT";
    std::string ser = "SER";
    // TODO: Add more edge cases

    Course mat266 = Course(&math, 266, 3); // "MAT266"
    Course ser222 = Course(&ser, 222, 3); // "SER222"
    REQUIRE(mat266.getCourseID() == "MAT266");
    REQUIRE(ser222.getCourseID() == "SER222");
    REQUIRE(ser222.getCourseID() != mat266.getCourseID());
}

/**
 * Verifies setDescription() accurately sets course description
 */
TEST_CASE("CourseTestCase3: setDescription() accurately sets Course description") {
    // TODO: Implement propper test cases
    std::string math = "MAT";
    std::string ser = "SER";
    Course mat266 = Course(&math, 266, 3); // "MAT266"
    Course ser222 = Course(&ser, 222, 3); // "SER222"

    REQUIRE(true);
}

/**
 * Test that adding prerequisites works when prereqs are added in "order"
 */
TEST_CASE("CourseTestCase4: addPrereqisite() works in order") {
    std::string ser = "SER";
    std::string cse = "CSE";

    Course ser334 = Course(&ser, 334, 3); // "SER334"
    Course ser315 = Course(&ser, 315, 3); // "SER315"
    Course ser316 = Course(&ser, 316, 3); // "SER316"
    Course cse230 = Course(&cse, 230, 3); // "CSE230"

    // ser334 has no prereqs
    REQUIRE(ser334.getPrereqs()->empty());

    // Add pre-reqs in "order"
    ser334.addPrereq(&cse230);
    ser334.addPrereq(&ser315);
    ser334.addPrereq(&ser316);

    // ser334 has prereqs
    REQUIRE(!(ser334.getPrereqs()->empty()));

    // SER334 has cse230, ser315, and ser316 as pre-reqs
    std::forward_list<Course*> list334 = {&cse230, &ser315, &ser316};
    std::forward_list<Course*> list334Reverse = {&ser316, &ser315, &cse230};
    REQUIRE(*(ser334.getPrereqs()) == list334); // == ordered list
    REQUIRE(*(ser334.getPrereqs()) != list334Reverse); // != reverse ordered list

    Course ser316Duplicate = Course(&ser, 316, 3);
    // Course prereq should only have unique elements
    ser334.addPrereq(&ser316Duplicate); // non-unique Course, unique ptr
    REQUIRE(*(ser334.getPrereqs()) == list334);
}

/**
 * Verify that adding prereqs in reverse order still results in a prerequisite list
 * in ascending order.
 */
TEST_CASE("CourseTestCase5: addPrereqisite() works in reverse insertion order") {
    std::string ser = "SER";
    std::string cse = "CSE";

    Course ser334 = Course(&ser, 334, 3); // "SER334"
    Course ser315 = Course(&ser, 315, 3); // "SER315"
    Course ser316 = Course(&ser, 316, 3); // "SER316"
    Course cse230 = Course(&cse, 230, 3); // "CSE230"

    // ser334 has no prereqs
    REQUIRE(ser334.getPrereqs()->empty());

    // Add pre-reqs in "order"
    ser334.addPrereq(&ser316);
    ser334.addPrereq(&ser315);
    ser334.addPrereq(&cse230);

    // ser334 has prereqs
    REQUIRE(!(ser334.getPrereqs()->empty()));

    // SER334 has cse230, ser315, and ser316 as pre-reqs
    std::forward_list<Course*> list334 = {&cse230, &ser315, &ser316};
    std::forward_list<Course*> list334Reverse = {&ser316, &ser315, &cse230};
    REQUIRE(*(ser334.getPrereqs()) == list334); // == ordered list
    REQUIRE(*(ser334.getPrereqs()) != list334Reverse); // != reverse ordered list
}

/**
 * Verifies that addPrerequisite() adds Course prerequisite Course ptrs in sorted
 * order, even when insertion order is inconsistent.
 */
TEST_CASE("CourseTestCase6: addPrereqisite() works out of order") {
    std::string math = "MAT";

    Course mat266 = Course(&math, 266, 3); // "MAT266"
    Course mat265 = Course(&math, 265, 3); // "MAT265"
    Course mat267 = Course(&math, 267, 3); // "MAT267"
    Course mat343 = Course(&math, 343, 3); // "MAT343"
    Course mat344 = Course(&math, 344, 3); // "MAT343"

    // mat267 has no prereqs
    REQUIRE(mat267.getPrereqs()->empty());

    // Add prereqs out of order
    mat267.addPrereq(&mat343); // first pre-req
    mat267.addPrereq(&mat265); // prepend list
    mat267.addPrereq(&mat344); // append list
    mat267.addPrereq(&mat266); // insert inbetween

    // mat267 has prereqs
    REQUIRE(!(mat267.getPrereqs()->empty()));

    // mat267 has sorted list of inserted prereqs
    std::forward_list<Course*> mat267List = {&mat265, &mat266, &mat343, &mat344};
    std::forward_list<Course*> mat267ListReverse = {&mat344, &mat343, &mat266, &mat265};
    REQUIRE(*(mat267.getPrereqs()) == mat267List);
    REQUIRE(*(mat267.getPrereqs()) != mat267ListReverse);
}

/**
 * Test that adding co-requisites works when coreqs are added in "order"
 */
TEST_CASE("CourseTestCase7: addCoreqisite() works in order") {
    std::string ser = "SER";
    std::string cse = "CSE";

    Course ser334 = Course(&ser, 334, 3); // "SER334"
    Course ser315 = Course(&ser, 315, 3); // "SER315"
    Course ser316 = Course(&ser, 316, 3); // "SER316"
    Course cse230 = Course(&cse, 230, 3); // "CSE230"

    // ser334 has no prereqs
    REQUIRE(ser334.getCoreqs()->empty());

    // Add pre-reqs in "order"
    ser334.addCoreq(&cse230);
    ser334.addCoreq(&ser315);
    ser334.addCoreq(&ser316);

    // ser334 has prereqs
    REQUIRE(!(ser334.getCoreqs()->empty()));

    // SER334 has cse230, ser315, and ser316 as pre-reqs
    std::forward_list<Course*> list334 = {&cse230, &ser315, &ser316};
    std::forward_list<Course*> list334Reverse = {&ser316, &ser315, &cse230};
    REQUIRE(*(ser334.getCoreqs()) == list334); // == ordered list
    REQUIRE(*(ser334.getCoreqs()) != list334Reverse); // != reverse ordered list

    Course ser316Duplicate = Course(&ser, 316, 3);
    // Course prereq should only have unique elements
    ser334.addCoreq(&ser316Duplicate); // non-unique Course, unique ptr
    REQUIRE(*(ser334.getCoreqs()) == list334);
}

/**
 * Verify that adding coreqs in reverse order still results in a co-requisite
 * list in ascending order.
 */
TEST_CASE("CourseTestCase8: addCoreqisite() works in reverse insertion order") {
    std::string ser = "SER";
    std::string cse = "CSE";

    Course ser334 = Course(&ser, 334, 3); // "SER334"
    Course ser315 = Course(&ser, 315, 3); // "SER315"
    Course ser316 = Course(&ser, 316, 3); // "SER316"
    Course cse230 = Course(&cse, 230, 3); // "CSE230"

    // ser334 has no prereqs
    REQUIRE(ser334.getCoreqs()->empty());

    // Add pre-reqs in "order"
    ser334.addCoreq(&ser316);
    ser334.addCoreq(&ser315);
    ser334.addCoreq(&cse230);

    // ser334 has prereqs
    REQUIRE(!(ser334.getCoreqs()->empty()));

    // SER334 has cse230, ser315, and ser316 as pre-reqs
    std::forward_list<Course*> list334 = {&cse230, &ser315, &ser316};
    std::forward_list<Course*> list334Reverse = {&ser316, &ser315, &cse230};
    REQUIRE(*(ser334.getCoreqs()) == list334); // == ordered list
    REQUIRE(*(ser334.getCoreqs()) != list334Reverse); // != reverse ordered list
}

/**
 * Verifies that addCorequisite() adds Course co-requisite Course ptrs in sorted
 * order, even when insertion order is inconsistent.
 */
TEST_CASE("CourseTestCase9: addCoreqisite() works out of order") {
    std::string math = "MAT";

    Course mat266 = Course(&math, 266, 3); // "MAT266"
    Course mat265 = Course(&math, 265, 3); // "MAT265"
    Course mat267 = Course(&math, 267, 3); // "MAT267"
    Course mat343 = Course(&math, 343, 3); // "MAT343"
    Course mat344 = Course(&math, 344, 3); // "MAT343"

    // mat267 has no coreqs
    REQUIRE(mat267.getCoreqs()->empty());

    // Add coreqs out of order
    mat267.addCoreq(&mat343); // first pre-req
    mat267.addCoreq(&mat265); // prepend list
    mat267.addCoreq(&mat344); // append list
    mat267.addCoreq(&mat266); // insert inbetween

    // mat267 has coreqs
    REQUIRE(!(mat267.getCoreqs()->empty()));

    // mat267 has sorted list of inserted coreqs
    std::forward_list<Course*> mat267List = {&mat265, &mat266, &mat343, &mat344};
    std::forward_list<Course*> mat267ListReverse = {&mat344, &mat343, &mat266, &mat265};
    REQUIRE(*(mat267.getCoreqs()) == mat267List);
    REQUIRE(*(mat267.getCoreqs()) != mat267ListReverse);
}

/**
 * Verifies that removePrereq() correctly removes pointer to Course pre-requisite
 */
TEST_CASE("CourseTestCase10: removePrerequisites() works as intended") {
    std::string ser = "SER";
    std::string cse = "CSE";

    Course ser334 = Course(&ser, 334, 3); // "SER334"
    Course ser315 = Course(&ser, 315, 3); // "SER315"
    Course ser316 = Course(&ser, 316, 3); // "SER316"
    Course cse230 = Course(&cse, 230, 3); // "CSE230"

    // ser334 has no prereqs
    REQUIRE(ser334.getPrereqs()->empty());

    // Add pre-reqs in "order"
    ser334.addPrereq(&cse230);
    ser334.addPrereq(&ser315);
    ser334.addPrereq(&ser316);

    // ser334 has prereqs
    REQUIRE(!(ser334.getPrereqs()->empty()));

    // SER334 has cse230, ser315, and ser316 as pre-reqs
    std::forward_list<Course*> list334 = {&cse230, &ser315, &ser316};
    REQUIRE(*(ser334.getPrereqs()) == list334); // == ordered list

    ser334.removePrereq(&ser315); // remove ser315
    // SER334 has cse230 and ser316 as pre-reqs
    std::forward_list<Course*> list334modified = {&cse230,&ser316};
    REQUIRE(*(ser334.getPrereqs()) == list334modified); // == ordered list

    ser334.removePrereq(&cse230); // remove ser316
    ser334.removePrereq(&ser316); // remove cse230

    // SER334 has no prerequisites
    std::forward_list<Course*> list334final = {};
    REQUIRE(*(ser334.getPrereqs()) == list334final); // == ordered list
    REQUIRE(ser334.getPrereqs()->empty());
}

/**
 * Verifies that removeCoreq() correctly removes pointer to Course co-requisite
 */
TEST_CASE("CourseTestCase11: removePrerequisites() works as intended") {
    std::string ser = "SER";
    std::string cse = "CSE";

    Course ser334 = Course(&ser, 334, 3); // "SER334"
    Course ser315 = Course(&ser, 315, 3); // "SER315"
    Course ser316 = Course(&ser, 316, 3); // "SER316"
    Course cse230 = Course(&cse, 230, 3); // "CSE230"

    // ser334 has no coreqs
    REQUIRE(ser334.getCoreqs()->empty());

    // Add pre-reqs in "order"
    ser334.addCoreq(&cse230);
    ser334.addCoreq(&ser315);
    ser334.addCoreq(&ser316);

    // ser334 has coreqs
    REQUIRE(!(ser334.getCoreqs()->empty()));

    // SER334 has cse230, ser315, and ser316 as co-reqs
    std::forward_list<Course*> list334 = {&cse230, &ser315, &ser316};
    REQUIRE(*(ser334.getCoreqs()) == list334); // == ordered list

    ser334.removeCoreq(&ser315); // remove ser315
    // SER334 has cse230 and ser316 as co-reqs
    std::forward_list<Course*> list334modified = {&cse230,&ser316};
    REQUIRE(*(ser334.getCoreqs()) == list334modified); // == ordered list

    ser334.removeCoreq(&cse230); // remove ser316
    ser334.removeCoreq(&ser316); // remove cse230

    // SER334 has no prerequisites
    std::forward_list<Course*> list334final = {};
    REQUIRE(*(ser334.getCoreqs()) == list334final); // == ordered list
    REQUIRE(ser334.getCoreqs()->empty());
}