//
// SDataBatch.hpp
//
// Author: J. Cardenzana
//
// Description:
//      This class is responsible for serving multiple data objects for use in
//      a training set.
//

#ifndef SDATABATCH_HPP
#define SDATABATCH_HPP

// STL HEADERS
#include <vector>

// SOS HEADERS
#include "SData.hpp"

class SDataBatch {
public:
    /* Constructors */
    SDataBatch(void);
    SDataBatch(const SDataBatch& other);
    virtual ~SDataBatch(void);

    /* Operators */
    SDataBatch operator=(const SDataBatch& other);

    /* Methods */
    SDataBatch* LoadNextBatch(const int& batchsize);

protected:
    /* Methods */
    void InitMembers(void);
    void CopyMembers(const SDataBatch& other);
    void FreeMembers(void);

    /* Variables */
    std::vector<SData*> s_data;         //!< Vector storing the actual data
    std::vector<std::vector<int>> s_classificaton; //!< Classification vectors

    bool s_has_classifiers;             //!< Specifies whether data has 
                                        //!< classifications

private:

};

#endif /* SDATABATCH_HPP */