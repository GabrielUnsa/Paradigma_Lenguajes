conexion(b,h,4).
conexion(h,f,9).
conexion(i,f,11).
conexion(f,g,10).
conexion(f,a,8).
conexion(a,b,7).
conexion(d,i,2).
tieneArista(X) :- conexion(X,_,_).
llegar(Inicio,Destino,Int,Costo):-  conexion(Inicio,Int,C1) , conexion(Int,Destino,C2) , Costo is C1+C2.
camino(X,Y):- conexion(X,Y,_).
camino(X,Y):- conexion(X,Z,_) , camino(Z,Y).
