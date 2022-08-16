in_room(bananas).
in_room(chair).
in_room(monkey).
dexterous(monkey).
tall(chair).
can_move(monkey,chair,bananas).
can_climb(monkey,chair).
get_on(X,Y) :- can_climb(X,Y).
under(Y,Z) :- in_room(X),in_room(Y),in_room(Z),can_move(X,Y,Z).
close(X,Z,Y) :- get_on(X,Y),under(Y,Z),tall(Y).%X toi gan Z thong qua Y
can_reach(X,Y,Z) :- dexterous(X),close(X,Y,Z).%X la loai kheo leo  va o gan Y thong qua Z
