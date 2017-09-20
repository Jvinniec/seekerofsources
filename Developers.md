# For Developers
This section is devoted to outlining appropriate good practices for those
wishing to expand on this code base.

## Formatting files
In the future, it would be nice to be able to run a linter over the code and
have that format all files in a uniform way. At the moment, that is far down
on the priority list. In the mean time, please stick as close as possible to
the formatting guidelines provided here.

### Class Name
Class names that are not specifically targetted to a particular instrument
should begin with `SS`. For example the dedicated training class is called
`SSTrainer`. 

### Data Members
Class data members should be all-lowercase. Also, all class data members
should begin with `s_` to identify it as a data member of the class.

### Brackets
This section describes appropriate bracket placement.

#### Class Methods
The opening bracket should be placed on a new line following the declaration
of the method. Similarly, the closing bracket should also be on it's own line
```cpp
/************************************************************************//**
 * @brief Brief description of function
 *
 * @param[in] param1        Description of @p param1
 * @param[in] param2        Description of @p param2
 * @return Description of return value
 *
 * Detailed description o f brief description is not sufficient.
 ****************************************************************************/
int SSClass::MyFunction(int param1,
                    int param2)
{ // <- Opening bracket on a new line
    /* Your code goes here */
} // <- Closing bracket on a new line
```