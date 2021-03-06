%Punto 1
madre(susana).
padre(tomas).
hijo(juan).
hombre(juan,tomas).
mujer(susana). %hechos
el_padre(juan,tomas).
la_madre(juan,susana).
los_padres(X, Y, Z):- el_padre(X,Z) , la_madre(X,Y). %reglas


%Notas de palindromos
fiesta.
palindromo(X):-reverse(X,X).

%Manejo de Lista
cuenta_elementos([],0).
cuenta_elementos([_|L],X):- cuenta_elementos(L,Tam) , X is Tam+1.
suma_lista([],0).
suma_lista([X|L],N):-suma_lista(L,C) , N is C+X.

%Punto 2
color_b(verde).
color(amarillo).
color(purpura).
planta_bien(X):- \+color_b(X).
deficiencia(crecimiento_atrofiado,nitrogeno).
deficiencia(borde_cafe,nitrogeno).
def(fosforo).
def(raiz,fosforo).
def(tallo_zanquivano,fosforo).
def(maduracion_retardada,fosforo).
defc(borde_quemado,potasio).
defc(tallos_debilatos,potasio).
defc(fruto,potasio).
defc(semilla,potasio).

planta_mal(X,Y):-deficiencia(X,Y).
planta_mal(X,Y,Z):-color(X),deficiencia(Y,Z).
planta_mal(X,Y):- def(X,Y).
planta_mal(X,Y):-color(X),def(Y).
planta_mal(X,Y):-defc(X,Y).
planta_mal(X,Y):-def(X,Y).

%Punto 3
incendio_A(papel).
incendio_A(madera).
incendio_A(tela).
incendio_B(liquidos_flamables).
incendio_B(aceite).
incendio_B(gas).
incendio_B(lubricante).
incendio_C(electrico).
incendio_D(magnesio).
incendio_D(sodio).
incendio_D(potasio).
extintor(absorcion_calor).
extintor(sustancia_quimicas).
ext(sustancias_secas).
ext(dioxido_carbono).
ext(bromotrifluorometano).
extin(espuma).
extor(trimetoxiboroxina).
extor(coque_grafitizado_cernido).

incendio(X,Y):-incendio_A(X),extintor(Y),print("Incendio de tipo A").
incendio(X,Y):-incendio_B(X),ext(Y), print("Incendio de tipo B").
incendio(X,Y):-incendio_B(X),extin(Y),print("Incendio de tipo B").
incendio(X,Y):-incendio_C(X),ext(Y),print("Incendio de tipo C").
incendio(X,Y):-incendio_D(X),extor(Y),print("Incendio de tipo D").

%Punto 5

sensor(ok1).
sensor(ok2).
sensor(ok3).
sensor(ok4).
sensor(ok5).
sensor(ok6).
sensor(ok7).
sensor(ok8).
sensor(ok9).
sensor(ok10).
sensor_mal(W,X,Y,Z):-sensor(W),sensor(X),sensor(Y),sensor(Z),print("El resto de los sensor en mal estado").

%Punto 7
padre(elena,arturo).
hermana(arturo,miriam).
madre(elena,monica).
masculino(arturo).
femenino(elena).
esposa(monica,arturo).
esposo(arturo,monica).

tia(X,Z):-padre(Y,X),hermana(Y,Z).
%tio(X,Z):-padre(Y,X),hermano(Y,Z).
%primo(X,Z):-tia(X,Y),hijo(Y,X).
%abuelo(X,Z):-padre(X,Y),padre(Y,Z).
%abuela(X,Z):-padre(X,Y),madre(Y,Z).
%progenitor(X,Y):-padre(X,Y).
%progenitor(X,Z):-padre(X,Y) , progenitor(Y,Z).

curso(prolog,horario(lunes,19),profesor(eduardo,morales),lugar(ccc,817)).
maestro(X,Y):-curso(X,horario,Y,lugar).
