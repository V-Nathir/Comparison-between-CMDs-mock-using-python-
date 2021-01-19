###########################
from def_P2_2 import *
from packages import *
###########################



head=['log(L)', 'log(Teff)', 'dist', 'M(Msun)', 'm(Msun)', 'Mbol', 'U','B', 'V', 'R', 'I', 'J', 'H', 'K', 'L', 'Li', 'M']
headIAC=['log(L)', 'log(Teff)', 'log(g)', 'mass_ini', 'massin','log(L)2', 'log(Teff)2', 'log(g)2', 'mass_ini2', 'massin2','age','Z', 'mass_2/mass_1', 'Mbol', 'U','B', 'V', 'R', 'I', 'J', 'H', 'K', 'L', 'L2', 'M']
print('---------------------------------------------------------------------')
print('-> Loading...')

cmd='bueno'
IAC=load(cmd,headIAC);print('->Cmd-Test: {}\n'.format(cmd))
Ref=load('cmd_Nalto.txt',head)

print('-> Loaded completed')
print('---------------------------------------------------------------------')

plot_raw(Ref['Color'],IAC['Color'],Ref['I'],IAC['I'],'Bruto')
valor=250
Xcell=np.linspace(min(Ref['Color']),2,valor);Ycell=np.linspace(4,-4,valor)
N_C_fila=valor-1
print('-> Plotting CMDs...')
plot_raw_one(Ref['Color'],Ref['I'],'Bruto_Ref')
plot_raw_one(IAC['Color'],IAC['I'],'Bruto_IAC')

mass(Ref['Color'],Ref['I'],Ref['m(Msun)'],Ref['M(Msun)'],'Ref_Masa',mod='final')
mass(IAC['Color'],IAC['I'],IAC['massin'],IAC['mass_ini'],'Test_Masa',mod='final')
mass(Ref['Color'],Ref['I'],Ref['m(Msun)'],Ref['M(Msun)'],'Ref_MasaInicial',mod='inicial')
mass(IAC['Color'],IAC['I'],IAC['massin'],IAC['mass_ini'],'Test_MasaInicial',mod='inicial')

age(IAC['Color'],IAC['I'],IAC['age'],'Edad_Test')
T(Ref['Color'],Ref['I'],Ref['log(Teff)'],'T_Ref')
print('Plotted')
print('---------------------------------------------------------------------')


print('Generando mallas...')
celdasIAC,max_longitud,n_celdas=empaquetado(IAC,Xcell,Ycell)
celdasRef,max_longitudRef,n_celdas=empaquetado(Ref,Xcell,Ycell)
print('Mallas generadas')

print('Valor de ocupación máximo de una celda para el test: {}'.format(max_longitud))
print('Valor de ocupación máximo de una celda para el modelo de referencia: {}'.format(max_longitudRef))
print('\n-> El número de celdas generado para la malla es de  {}'.format(n_celdas))
print('---------------------------------------------------------------------')

min_IAC,max_IAC=distribucion_one(Xcell,Ycell,max_longitud,celdasIAC,'IAC')
print('\n-> Mínimo de opucación por celda para el CMD-test en log10 {}'.format(round(min_IAC,4)))
print('-> Máximo de opucación por celda para el CMD-test en log10 {}\n'.format(round(max_IAC,4)))

min_Ref,max_Ref=distribucion_one(Xcell,Ycell,max_longitudRef,celdasRef,'Ref')

print('\n-> Mínimo de opucación por celda para el CMD-referencia en log10 {}'.format(round(min_Ref,4)))
print('-> Máximo de opucación por celda para el CMD-referencia en log10 {}\n'.format(round(max_Ref,4)))

distribucion(Xcell,Ycell,max_longitud,max_longitudRef,celdasIAC,celdasRef)
if min_Ref>min_IAC:
	minimo=min_IAC
	print('\nEl valor de ocupación mínimo en log10 de una celda es: {}'.format( round(minimo,4)))
if min_IAC>min_Ref:
	minimo=min_Ref
	print('El valor de ocupación mínimo en log10 de una celda es: {}'.format(round(minimo,4)))
else:
	minimo=min_Ref
	print('El valor de ocupación mínimo en log10 de una celda es: {}'.format(round(minimo,4)))


if max_IAC>max_Ref:
	maximo=max_IAC
	print('\nEl valor de ocupación máximo en log10 de una celda es: {}'.format( round(maximo,4)))
if max_Ref>=max_IAC:
	maximo=max_Ref
	print('El valor de ocupación máximo en log10 de una celda es: {}'.format(round(maximo,4)))


pesoUP,pesoIN,pesoDown,residuosx,residuosy,residuosIAC,residuosRef,residuoceldas,celdasocupadas,maximoC=plotmallado(Xcell,Ycell,Ref['I'],Ref['Color'],celdasIAC,celdasRef,minimo,maximo,N_C_fila)
print('Pesos: \n .- <1 ; {} \n .- >1 & <2 ; {} \n .- >2 ; {}'.format(pesoDown,pesoIN,pesoUP))
print('\nNúmero de celdas ocupadas: {}'.format(maximoC))
print('---------------------------------------------------------------------')

print('Valor de celdas de tipo residuo en el primer procesado: {}'.format(round(celdasocupadas,5)))
print('---------------------------------------------------------------------')



celdasocupadasIAC,conteodistribucionIAC=plotmallado_one(Xcell,Ycell,Ref['I'],Ref['Color'],celdasIAC,minimo,maximo,'IAC')
print('Las celdas ocupadas para el CMD test son {}'.format(celdasocupadasIAC))
print('Las celdas con caracter aleatorio para el CMD test son {}'.format(conteodistribucionIAC))

celdasocupadasRef,conteodistribucionRef=plotmallado_one(Xcell,Ycell,Ref['I'],Ref['Color'],celdasRef,minimo,maximo,'Ref')
print('Las celdas ocupadas para el CMD referencia son {}'.format(celdasocupadasRef))
print('Las celdas con caracter aleatorio para el CMD referencia son {}'.format(conteodistribucionRef))

print('---------------------------------------------------------------------')

if np.absolute(conteodistribucionIAC-conteodistribucionRef)<0.3*maximoC:
	post=postprocesado(pesoUP,pesoIN,pesoDown,Xcell,Ycell,Ref['I'],Ref['Color'],minimo,maximo,residuosx,residuosy,residuosIAC,residuosRef,residuoceldas,celdasIAC,celdasRef,n_celdas)
	print('\nValor de celdas de tipo residuo en el post-procesado {}'.format(round(post,5)))
	alfa='yes'
else: 
	alfa='no'
print('---------------------------------------------------------------------')
print('El cálculo del residuo se pesa con el máxmimo número de celdas ocupadas: {}\n'.format(maximoC))
print('El residuo generado por el primer procesamiento es: {}'.format(round(celdasocupadas/maximoC,5)))
if alfa=='yes':
	print('El residuo generado por el post-procesamiento es: {}'.format(round(post/maximoC,5)))
else: 
	print('No se ha realizado postprocesado debido a la poca similitud en la cantidad de celdas de regiones dispersas.')
print('Diferencia de celdas entre CMDs respecto al total de ocupación: {}'.format(round(np.absolute(celdasocupadasIAC-celdasocupadasRef)/maximoC,4)))
print('---------------------------------------------------------------------')
