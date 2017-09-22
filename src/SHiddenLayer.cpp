//
// SHiddenLayer.cpp
//
// Author: J.V. Cardenzana
//
// Description
//      Defines a hidden layer in the CNN
//
#include "SHiddenLayer.hpp"

//=========================================================================//
// Constructors / Deconstructor
//=========================================================================//

/************************************************************************//**
 * @brief Default constructor
 ****************************************************************************/
SHiddenLayer::SHiddenLayer(void)
{
}


/************************************************************************//**
 * @brief Copy Constructor
 *
 * @param[in] other             Object to be copied
 ****************************************************************************/
SHiddenLayer::SHiddenLayer(const SHiddenLayer& other)
{
    CopyMembers(other);
}


/************************************************************************//**
 * @brief Destructor
 ****************************************************************************/
SHiddenLayer::~SHiddenLayer(void)
{
    FreeMembers();
}


//=========================================================================//
// Public Methods
//=========================================================================//


//=========================================================================//
// Protected Methods
//=========================================================================//

/************************************************************************//**
 * @brief Initialize the data members
 ****************************************************************************/
void SHiddenLayer::InitMembers(void)
{
    // Define the scope of this object
    s_scope = tensorflow::Scope::NewRootScope();
}


/************************************************************************//**
 * @brief Copy data members
 ****************************************************************************/
void SHiddenLayer::CopyMembers(const SHiddenLayer& other)
{
    FreeMembers();

    // Copy scope of this object
    s_scope = other.Scope();
}


/************************************************************************//**
 * @brief Deallocate memory
 ****************************************************************************/
void SHiddenLayer::FreeMembers(void)
{

}