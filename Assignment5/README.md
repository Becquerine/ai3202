The command to run my Assignment 5 program is as follows:

python3 Assignment5.py World1MDP.txt 0.5

You may replace World1MDP.txt with another suitable world text file (must have 8x10 dimensions), and 0.5 with another floating-point epsilon value.

Questions to answer:

I found that just as I had increased epsilon to 9.0, my optimal path changed. Originally, my path followed through the middle of the world, moving around mountains (but walking through a snake for some reason) and passing through a barn. When I increased my epsilon to 9, I noticed that the path followed farther east to tread over a different snake. When I increased epsilon to 11, I noticed my path moved north, stumbling through many mountain ranges it could have easily avoided. After that, any increases to epsilon did not alter my "optimal" path very much. As I increase epsilon, the tolerance for error in the Value Iteration process grows, and my path becomes less and less optimal.

I would like to make one note: for some reason, my most optimal path (with epsilon = 0.5 and similar values) leads the horse through a snake. I find this strange because the horse could easily move further east and pass through a mountain instead of a snake. I have checked my program, and I cannot find anything obviously wrong. Either my algorithm is slightly incorrect, or my algorithm knows better and found a more likely hazard in the alternate path.
