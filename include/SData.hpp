//
// SData.hpp
//
// Author: J. Cardenzana
//
// Description:
//      This class is responsible for serving a single data object for use in
//      SoS. SData is a base class from which a dedicated data class can be
//      developed for a specific sample of images.
//

#ifndef SDATA_HPP
#define SDATA_HPP

class SData {
public:
    /* Constructors */
    SData(void);
    SData(const SData& other);
    virtual ~SData(void);

    /* Operators */

    /* Methods */
    virtual bool Load(void) = 0;
    virtual bool Clear(void);

    /* Variables */

protected:

    /* Methods */
    void InitMembers(void);
    void CopyMembers(const SData& other);
    void FreeMembers(void);

    /* Variables */


private:

};

#endif /* SDATA_HPP */