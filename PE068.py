#No code is needed:
#the problem states that we are trying to find the largest 16 digit string.
#We know that we write the solution out starting at the lowest, exterior node. So in the example, 4 starts because 4 < 5 and 6
#knowing this, we can plug in 10, 9, 8, 7, and 6 on the exterior nodes since we want the first digit to be as large as possible(6)
#We also know the string goes clockwise. For that reason we put 10, closest to 6 then 9 and so forth
#from here, we look to place 1, we know the 1 will likely need to be in the 10 group, from there we can choose to place it
#in the 6 group or 9 group after some guess and check, having 6 and 1 in the same group would be too small a sum so 1 goes at the node
#intersecting 9 and 10 from there we solve 2 we know it can't go in the 9 or 10 group or the sum would be too small, so we look to place it
#in the 7 and 6 intersection or 7 and 8 intersection since 2 is small, we place it at the 7 and 8 intersection
# from here, we place 3. we know 3 can't go at the 9 and 8 intersection since there sums would not be equal, and it can't go at the
#7 and 6 intersection for the same reason, so we put it at the 10 and 6 intersection from there we fill everything out and write the string
# as directed

