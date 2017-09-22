//
// STrainer.hpp
//
// Author: J. Cardenzana
//
// Description:
//    Implements the training algorithm for a CNN specifically for searching
//    astronomy images for sources.
//

#ifndef STRAINER_HPP
#define STRAINER_HPP

#include <string>
#include <vector>

// SOS CLASSES
#include "SDataBatch.hpp"
#include "SGraph.hpp"

class STrainer {
public:
    /* Constructors/Destructor */
    STrainer(void);
    STrainer(const SSGraph& graph);
    STrainer(const SSTrainer& other);
    virtual ~STrainer(void);

    /* Operators */


    /* Methods */
    void SaveModel(const std::string& filename);
    void TrainModel(const SDataBatch& data);

    /* Variables */

protected:

    /* Methods */
    void InitMembers(void);
    void CopyMembers(const STrainer& other);
    void FreeMembers(void);

    /* Variables */
    SGraph s_graph;            //!< TensorFlow graph

private:

    /* Methods */

    /* Variables */

};

#endif /* STRAINER_HPP */