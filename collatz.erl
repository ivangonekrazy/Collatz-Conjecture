-module(collatz).
-export([sequence/1]).

sequence( X ) -> sequence(X, []).

sequence( 1, _ )     -> [1];
sequence( X, [] )    -> sequence(X, [X]);
sequence( X, [H|T] ) ->
  case (X rem 2) of
    0 -> [ H | sequence( X div 2,   T) ];
    1 -> [ H | sequence( X * 3 + 1, T) ]
  end.

