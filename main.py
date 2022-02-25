##Ramzi L.
### In this lab, we're going to get experience building more complex models, generating
### random numbers, writing functions and creating loops. There are 8 questions for you to finish - each is
### numbered in the comments.

### Suppose that we want to model a bikeshare, as we see in Chapter 2 of Modeling and Simulation in Python.
### We're going to tweak it a little.

### We'll have one set of bikes at USF, and another set at Ocean Beach.
### Let's make variables for each of them. Assume we start with 10 bikes in each location.

bikesAtUSF = 10
bikesAtOceanBeach = 10

### This is fine, but keeping track of two separate variables is a headache. Let's instead group them together in
### a list which we'll call bikes.

bikes = [bikesAtUSF, bikesAtOceanBeach]

### We can acccess the elements of a list through an index. Let's print out the number of bikes at USF.

print("Bikes at USF %d" % bikes[0])

### 1. How do we print the number of bikes at Ocean Beach? Write a statement to do this.

print("Bikes at Ocean Beach: %d" % bikes[1])

#### -------------------

### When a person rides from USF to Ocean Beach, there is one less bike at USF, and one more at Ocean Beach.
### Let's write a function to manage this.

def bikeToOceanBeach(bikeList):
    bikeList[0] = bikeList[0] - 1
    bikeList[1] = bikeList[1] + 1


### 2. Write a similar function called bikeToUSF that adds one bike to USF and removes one from Ocean Beach.

def bikeToUSF(bikeList):
    bikeList[0] = bikeList[0] + 1
    bikeList[1] = bikeList[1] - 1


### ---------------------

### What if there are no bikes at a location? We don't want to have negative bikes! Let's account for the fact
### that if a user shows up at a location and there are no bikes, they don't go anywhere. If there's zero bikes,
### we'll just return without changing anything.



### 3. Make a similar fix to bikeToUSF. Change the test in the conditional so that if it is true,
### you update the counts and if it's false you just return.


### 4. Let's make a print function that can nicely display the number of bikes in each location. Call it printBikes.
###  It should use the print statements that we created in step 1.

def printBikes(bikeList):
    print("Bikes at USF %d" % bikeList[0])
    print("Bikes at Ocean Beach %d" % bikeList[1])


### --------------------------

### Now, we need a way to randomly choose whether someone will arrive to get a bike at a particular time.

### Python has a random library that can help us out. Let's import that.

import random


### now, let's write a function that will tell us whether there is a customer or not. It will take a threshold as input.
# If the random number is less than the threshold, return True. If it's greater, return False.

def customerAvailable(threshold):
    value = random.random()
    if value < threshold:
        return True
    else:
        return False


### Now we're ready to try it out. Let's start with a single episode. Assume that the threshold is 0.5.

bikeList = [10, 10]
threshold = 0.5
printBikes(bikeList)
### first we'll do USF:
if (customerAvailable(threshold)):
    bikeToOceanBeach(bikeList)

if (customerAvailable(threshold)):
    bikeToUSF(bikeList)

printBikes(bikeList)

### 5. What if people arrive at the locations at different rates?
### Replace threshold with two variables: USF_threshold and ocean_beach_threshold

for i in range(10):
    USFThreshold = 0.7
    OceanBeachThreshold = 0.3
    if (customerAvailable(USFThreshold)):
        bikeToOceanBeach(bikeList)

    if (customerAvailable(OceanBeachThreshold)):
        bikeToUSF(bikeList)

    printBikes(bikeList)

### ----------------------------------------

### We've gone through one round, but what if we want to do lots of rounds?
### We do this through iteration.
# Now, take the code we wrote above and put it inside the loop.
### I'll get you started.