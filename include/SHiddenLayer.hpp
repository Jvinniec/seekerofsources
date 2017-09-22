//
// SHiddenLayer.hpp
// 
// Author: J.V. Cardenzana
//
// Description
//      Define a hidden layer in the CNN.
//

#ifndef SHIDDENLAYER_HPP
#define SHIDDENLAYER_HPP

// STL HEADERS
#include <string>

// TENSORFLOW HEADERS
#include "tensorflow/cc/client/client_session.h"
#include "tensorflow/cc/ops/standard_ops.h"
#include "tensorflow/core/framework/tensor.h"

using namespace tensorflow;
using namespace tensorflow::ops;

class SHiddenLayer {
public:
    /* Constructors/Deconstructor */
    SHiddenLayer(void);
    SHiddenLayer(const SHiddenLayer& other);
    virtual ~SHiddenLayer(void);

    /* Operators */

    /* Methods */
    void                 InMatrix(const MatMult& matrix);
    tensorflow::MatMult& OutMatrix(void);
    tensorflow::Scope&   Scope(void);
    /* Variables */

protected:

    /* Methods */
    void InitMembers(void);
    void CopyMembers(const SSHiddenLayer& other);
    void FreeMembers(void);

    /* Variables */
    
    tensorflow::Scope s_scope;              //!< Scope of this layer

private:

};


/************************************************************************//**
 * @brief Return the scope of this layer
 *
 * @return Scope of this layer
 ****************************************************************************/
inline
tensorflow::Scope& SHiddenLayer::Scope(void)
{
    return s_scope;
}

#endif /* SHIDDENLAYER */

