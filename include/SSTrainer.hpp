//
// SSTrainer.hpp
//
// Author: J. Cardenzana
//
// Description:
//    Implements the training algorithm for a CNN specifically for searching
//    astronomy images for sources.
//

#ifndef SSTRAINER_HPP
#define SSTRAINER_HPP

#include <string>
#include <vector>

// SOS CLASSES
#include "SSDataBatch.hpp"
#include "SSGraph.hpp"

class SSTrainer {
public:
    /* Constructors/Destructor */
    SSTrainer(void);
    SSTrainer(const SSGraph& graph);
    SSTrainer(const SSTrainer& other);
    virtual ~SSTrainer(void);

    /* Operators */


    /* Methods */
    void SaveModel(const std::string& filename);
    void TrainModel(const SSDataBatch& data);

    /* Variables */

protected:

    /* Methods */

    /* Variables */
    SSGraph s_graph;            //!< TensorFlow graph

private:

    /* Methods */

    /* Variables */

};

#endif /* SSTRAINER_HPP */