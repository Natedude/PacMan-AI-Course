check drawing it prints out

maybe update ilearn post?

***     Bug: Suboptimal moves
***     State:
***     %%%%%%%%%%%%%%%%%%%%
***     %      %    %   ...%
***     % %%   %%  %%   %%.%
***     % %  %        %.o%.%
***     % %% % %%%%%% %.%%.%
***     %        >G G .....%
***     %%%%%%%%%%%%%%%%%%%%
***     Score: 536
***
***     Student Move:East
***     Optimal Move:West

look at move 84, 85, and 144

ok so the move it doesn't like is move 84.
	-found from returning 'Test' at 84th move

the weird thing to note is that while watching that test, the pacman always moves west and never east, even when getAction returns East