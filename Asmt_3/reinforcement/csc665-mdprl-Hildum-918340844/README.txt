# Nathan Hildum = 918 340 844

## Hours spent ~ 16-32

---

## Implementation

### Q1,2,31

At first I tried to do the entire value iteration in one method, not realizing the compute___ methods were there to spread out the work of the algorithm in some clever ways. Once I realized how to use the two compute___ methods, I then also realized I could make the best(s) method. The best(s) method condenses the work of finding weighted averages, max, and argMax values. This simplified other methods and avoided repeat code.

### Q6,7,8,9,10

I reused the idea for a best(s) method, instead calling it findBest(s). Other than that, I tried to implement the algorithm as close to the update equations from the class materials. Also, I tried to separate big equations into separate lines so it is more readable.