//
// SSDataBatch.hpp
//
// Author: J. Cardenzana
//
// Description:
//      This class is responsible for serving multiple data objects for use in
//      a training set.
//

#ifndef SSDATABATCH_HPP
#define SSDATABATCH_HPP

#include "SSData.hpp"

class SSDataBatch {
public:
    /* Constructors */
    SSDataBatch(void);
    SSDataBatch(const SSDataBatch& other);
    virtual ~SSDataBatch(void);

    /* Operators */
    SSDataBatch operator=(const SSDataBatch& other);

    /* Methods */
    bool LoadNextBatch(const int& batchsize);

    /* Variables */

protected:

    /* Variables */

    /* Methods */


private:

};

#endif /* SSDATABATCH_HPP */