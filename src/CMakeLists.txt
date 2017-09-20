
#------------------------------------------
# Define include directories
#------------------------------------------
include_directories (${CMAKE_CURRENT_SOURCE_DIR}/../include)

#------------------------------------------
# Define the source and header files needed
# by the SeekerOfSources library
#------------------------------------------
set (sos_SOURCES
    SSData.cpp
    SSTrainer.cpp
    )

set (sos_HEADERS
    ../include/SSData.hpp
    ../include/SSTrainer.hpp
    )

#------------------------------------------
# Create both a static and shared version of the library
#------------------------------------------
add_library (sosources SHARED ${sos_SOURCES} ${sos_HEADERS})
add_library (sosources_static STATIC ${sos_SOURCES} ${sos_HEADERS})

# Make sure the static version has the same name
set_target_properties(sosources_static PROPERTIES OUTPUT_NAME sosources)

#------------------------------------------
# Executables
#------------------------------------------


#------------------------------------------
# Link the library
#------------------------------------------
target_link_libraries(sosources)
