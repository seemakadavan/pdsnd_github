# Dummy file

# Function Definitions

# Returns total travel time for the dataset
sumOfTravelTime <- function(dataset) {
   sum(dataset$Trip.Duration / 60, na.rm = TRUE) 
}


