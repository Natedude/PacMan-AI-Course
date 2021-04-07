# Nathan Hildum = 918 340 844

## ~ Hours spent

16-32

---
## Q1 - ReflexAgent
I compared the given game state and the generated successor state to calculate if Pac-man is moving away from the nearest ghost or moving towards the nearest food. When ghosts are not too close, the only focus is getting closer to the closest food. Once a ghost gets too close, then the only focus is on getting farther away from the closest ghost.

---
## Q2 - Minimax
I implemented this using modular methods like the psuedocode given in class. This also made it so I could put a lot of code in the MultiSearchAgent parent to be shared by the other agents.

---
## Q4 - Expectimax
Works the same as the Minimax, except the agentType() function now tells ghosts to use the expected value function instead of the minimize value function.

I got this working and it passes all the tests except one:
`python autograder.py  -t test_cases/q4/7-pacman-game `

I have made some progress on pinpointing where the error is coming from though. It seems that the test's feedback is saying getAction() returned an **East** action when it should have returned a **West** action. The action the feedback is referring to happens on the **84th** call to getAction() for that test.

Something odd, though, happens when I run the test with graphics shown and I pinpoint the exact moment when my Pac-man should be (incorrectly) going **East**.

I can see that **it actually goes West**, even when my getAction() returns an **East**... Weird...

---
## Q5
Give inf and -inf scores if state is a win or lose. After that, I wanted
to choose a number of variables that I could multiply by weights and sum
to get a score that works better than the normal score. I thought it would
be cool to be able to play with the weights to find an optimal set of weights. (It might even be fun to figure out some kind of learning system that could find the optimal weights)

### Food:
The food left uneaten and the distance to the nearest food should
both decrease the score. This encourages eating more food and getting closer to
the nearest food.

### Capsules:
We want to subtract the number of capsules left uneaten from the score
so that Pac-man will eat one if he gets a chance. I did not include a variable relating
the distance to the closest capsule so that Pac-man wasn't constantly trying to chase them.

### Ghosts:
I make lists of the scared ghosts and the active ghosts by checking their scaredTimer fields. We want to minimize the distance to the closest scared ghost, so the larger the distance, the more is subtracted from the score.

The closer the closest ghost is, the lower the score should be. So we want to subtract the most when the distance is smallest. The reciprocal of the distance is used for this. Pac-man wants to widen the distance to minimize the amount subtracted from the score.

With these two relations to ghosts, Pac-man will be pulled towards scared ghosts,
but pushed away from active ghosts.