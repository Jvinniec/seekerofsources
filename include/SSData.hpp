//
// SSData.hpp
//
// Author: J. Cardenzana
//
// Description:
//      This class is responsible for serving a single data object for use in
//      SoS.
//

#ifndef SSDATA_HPP
#define SSDATA_HPP

class SSData {
public:
    /* Constructors */
    SSData(void);
    SSData(const SSData& other);
    virtual ~SSData(void);

    /* Operators */
    SSData operator=(const SSData& other);

    /* Methods */

    /* Variables */

protected:

    /* Variables */

    /* Methods */


private:

};

#endif /* SSDATA_HPP */