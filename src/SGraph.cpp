//
// SGraph.cpp
//
// Author: J. Cardenzana
//
// Description
//      Constructs the TensorFlow graph
//

#include "SGraph.hpp"


//=========================================================================//
// Constructors / Deconstructor
//=========================================================================//

/************************************************************************//**
 * @brief Default constructor
 ****************************************************************************/
SGraph::SGraph(void)
{

}


/************************************************************************//**
 * @brief Copy constructor
 ****************************************************************************/
SGraph::SGraph(const SGraph& other)
{
    // Copy data members from 'other'
    CopyMembers(other);
}


/************************************************************************//**
 * @brief Deconstructor
 ****************************************************************************/
SGraph::~SGraph(void)
{
    // Free allocated objects
    FreeMembers();
}

//=========================================================================//
// Public Members
//=========================================================================//

/************************************************************************//**
 * @brief Add a hidden layer to the graph at the end
 *
 * @param[in] layer             User defined hidden layer
 *
 * This method adds a hidden layer to the graph. Any layers added previously
 * serve as inputs to this layer
 ****************************************************************************/
void SGraph::AddHiddenLayer(const SHiddenLayer& layer)
{

}


/************************************************************************//**
 * @brief Initialize the actual graph object (AFTER adding layers)
 ****************************************************************************/
void SGraph::InitGraph(void)
{
    if (HiddenLayers() == 0) {
        // TODO: Throw an error (exception?)
    }
}


/************************************************************************//**
 * @brief Get the information about this object
 *
 * @return A string containing the information about this object
 ****************************************************************************/
std::string SGraph::Print(void)
{
    std::string graph_info
}


//=========================================================================//
// Protected Members
//=========================================================================//


/************************************************************************//**
 * @brief Initialize data members
 ****************************************************************************/
void SGraph::InitMembers(void)
{

}


/************************************************************************//**
 * @brief Copy data members
 ****************************************************************************/
void SGraph::CopyMembers(const SGraph& other)
{
    FreeMembers();
}


/************************************************************************//**
 * @brief Free data members
 ****************************************************************************/
void SGraph::FreeMembers(void)
{

}