//
// SSGraph.hpp
//
// Author: J. Cardenzana
//
// Description
//      Constructs the TensorFlow graph
//

#ifndef SSGRAPH_HPP
#define SSGRAPH_HPP

// C++ STL LIBS
#include <string>

// TENSORFLOW
#include "tensorflow/cc/client/client_session.h"

// SOS CLASSES
#include "SSHiddenLayer.hpp"

class SSGraph {
public:
    /* Constructors/Destructor */
    SSGraph(void);
    SSGraph(const SSGraph& other);
    virtual ~SSGraph(void);

    /* Methods */
    void AddHiddenLayer(const SSHiddenLayer& layers);
    int  HiddenLayers(void);
    void InitGraph(void);
    std::string Print(void);

    /* Variables */

protected:

    /* Methods */
    void InitMembers(void);
    void CopyMembers(void);
    void FreeMembers(void);
    
    /* Variables */
    int s_hiddenlayers;             //!< Specifies number of hidden layers

private:

};

/************************************************************************//**
 * @brief Get the number of hidden layers in the network
 *
 * @return Number of hidden layers
 ****************************************************************************/
 inline
 int SSGraph::HiddenLayers(void)
 {
     return s_hiddenlayers;
 }

#endif /* SSGRAPH_HPP */