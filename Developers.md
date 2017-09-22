# Overview
This file is devoted to outlining appropriate good practices for those
wishing to expand on this code base.

# Formatting files
In the future, it would be nice to be able to run a linter over the code and
have that format all files in a uniform way. At the moment, that is far down
on the priority list. In the mean time, please stick as close as possible to
the formatting guidelines provided here.

# Classes

## Class Name
Class names that are not specifically targetted to a particular implementation
should begin with `S`. For example the dedicated training class is called
`STrainer`.

## Data Members
Class data members should be all-lowercase. This criteria is meant to 
distinguish variables from  methods in a class.Also, all class data members
should begin with `s_` to identify it as a data member of the class. Ideally,
class data members are all declared as protected members with public functions
that allow the user to update or access their values if necessary.

# Methods/Function

## Documentation / Help Information (Doxygen format)
A description of the method should be provided immediately preceeding the
method in the associated class' `.cpp` file. It should begin with a brief
one line description of the method, followed by the parameter descriptions,
followed by the return value description (if there is one). If the brief 
description is insufficient to really describe the functionality of the method,
then you can provide a detailed description at the end of this block. An
example of this is as follows:
```cpp
/************************************************************************//**
 * @brief Brief one line function description
 *
 * @param[in]  input_param       Description of @p param1
 * @param[out] updated_param     Description of @p param2
 * @return Description of return value
 *
 * Detailed description if brief description is not sufficient. This 
 * description can span multiple lines if necessary. See the doxygen
 * documentation for more information.
 ****************************************************************************/
```

Class variables should be documented in the class' associated `.hpp` file. Each
description should be begin with `//!<`. For example:
```cpp
#include <vector>
class SMyClass {
public:
    /* Constructors and variable access methods */
protected:
    /* Variables */
    int              s_var1;    //!< An integer parameter
    double           s_var2;    //!< A double parameter
    std::vector<int> s_vect;    //!< A vector parameter
};
```

## Brackets 
The opening bracket should be placed on a new line following the declaration
of the method. Similarly, the closing bracket should also be on it's own line

## Example
The following is an example class method outline that
```cpp
/************************************************************************//**
 * @brief Brief description of function
 *
 * @param[in] param1        Description of @p param1
 * @param[in] param2        Description of @p param2
 * @return Description of return value
 *
 * Detailed description if brief description is not sufficient.
 ****************************************************************************/
int SMyClass::MyFunction(int param1,
                         int param2)
{                                           // <- Opening bracket on a new line
    /* Your code goes here */
    return value;
}                                           // <- Closing bracket on a new line
```

# General