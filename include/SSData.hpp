//
// SSData.hpp
//
// Author: J. Cardenzana
//
// Description:
//      This class is responsible for serving a single data object for use in
//      SoS. SSData is a base class from which a dedicated data class can be
//      developed for a specific sample of images.
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

    /* Methods */
    virtual bool Load(void) = 0;
    virtual bool Clear(void);

    /* Variables */

protected:

    /* Variables */

    /* Methods */


private:

};

#endif /* SSDATA_HPP */