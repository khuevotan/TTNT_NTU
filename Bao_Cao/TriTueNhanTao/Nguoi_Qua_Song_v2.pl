trans([A,B,C,D,1],[X,Y,Z,T,0]):-A>0,B>0,X is A-1,Y is B-1, Z is C+1, T is D+1.
trans([A,B,C,D,0],[X,Y,Z,T,1]):-C>0,D>0,X is A+1,Y is B+1, Z is C-1, T is D-1.

trans([A,B,C,D,0],[X,B,Z,D,1]):-C>1,X is A+2,Z is C-2.
trans([A,B,C,D,1],[X,B,Z,D,0]):-A>1,X is A-2,Z is C+2.  

trans([A,B,C,D,1],[A,Y,C,T,0]):-B>1,Y is B-2,T is D+2.
trans([A,B,C,D,0],[A,Y,C,T,1]):-D>1,Y is B+2,T is D-2.

trans([A,B,C,D,0],[X,B,Z,D,1]):-C>0,X is A+1,Z is C-1.
trans([A,B,C,D,1],[X,B,Z,D,0]):-A>0,X is A-1,Z is C+1.

trans([A,B,C,D,0],[A,Y,C,T,1]):-D>0,Y is B+1,T is D-1.
trans([A,B,C,D,1],[A,Y,C,T,0]):-B>0,Y is B-1,T is D+1.


dangers([A,B,C,D,_]):-A>=B,C>=D.
dangers([A,B,0,_,_]):-A>=B.
dangers([0,_,A,B,_]):-A>=B.

goal([0,0,3,3,0]).