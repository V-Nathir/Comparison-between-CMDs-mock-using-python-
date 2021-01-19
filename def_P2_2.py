###################
from packages import *

###################

def load(name,head):
	A=np.loadtxt('cmd/'+name)
	B=pd.DataFrame(A,columns=head)
	C=np.linspace(1,len(B),len(B))
	B.insert(0,"ID",C,True)
	B.insert(1,"Color",B['V']-B['I'],True)
	return(B)


def distribucion_one(Xcell,Ycell,valorcelda,infoceldas,name):
	A=[]
	conceldas=0
	Progress = ChargingBar('Calculating distribution...', max=len(Ycell)-1)

	for i in range(len(Ycell)-1):
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
		for j in range(len(Xcell)-1):
				
			if len(infoceldas[conceldas])==0 :
				conceldas+=1
			
			else:
				buf=np.log10(len(infoceldas[conceldas]) ) 
				A.append(buf)
				conceldas+=1
	A=np.array(A)
	B=np.linspace(1,len(A),len(A))
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.hist(A,color='lime',edgecolor='green', linewidth=5)
	plt.grid()
	plt.xlabel('Valor de la celda',fontsize=20)
	plt.ylabel('Frecuencia absoluta',fontsize=20)
	plt.savefig('DistribuciónCeldas_'+name+'.png')
	plt.close()
	Progress.finish()

	return(np.min(A),np.max(A))


def distribucion(Xcell,Ycell,valorcelda,valorcelda2,infoceldas,infoceldas2):
	A=[]
	conceldas=0
	Progress = ChargingBar('Calculating distribution...', max=len(Ycell)-1)

	for i in range(len(Ycell)-1):
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
		for j in range(len(Xcell)-1):
			if len(infoceldas[conceldas])-len(infoceldas2[conceldas])==0:
				conceldas+=1
				continue
			else:
				buf=(np.absolute(len(infoceldas[conceldas])-len(infoceldas2[conceldas]) )) 
				A.append(buf)
				conceldas+=1
	A=np.log10(np.array(A))
	A.sort()
	B=np.linspace(1,len(A),len(A))
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.hist(A,color='lime',edgecolor='green', linewidth=5)
	plt.grid()
	plt.xlabel('Valor de la celda en log10',fontsize=20)
	plt.ylabel('Frecuencia absoluta',fontsize=20)
	plt.savefig('DistribuciónCeldas.png')
	plt.close()
	Progress.finish()





def plot_raw_one(color1,y1,name):
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')


	plt.plot(color1,y1,'o',color='lime',markersize=0.2)

	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Synthetic CMD \'mock\' ',fontsize=20)
	ax.set_ylim(max(y1),min(y1))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)

	plt.savefig(name+'.png')
	plt.close()

def plot_raw(color1,color2,y1,y2,name):
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')


	plt.plot(color1,y1,'o',color='lime',markersize=0.2)


	plt.plot(color2,y2,'o',color='magenta',markersize=0.2)

	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Synthetic CMD \'mock\' ',fontsize=20)
	ax.set_ylim(max(y1),min(y1))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)

	plt.savefig(name+'.png')
	plt.close()

def plotmallado(Xcell,Ycell,ylim,xlim,infoceldas,infoceldas2,minimo,maximo,N_fila):
	Progress = ChargingBar('Processing:', max=len(Ycell)-1)
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')

	cm1 = mcol.LinearSegmentedColormap.from_list("Cantidad de puntos. Escala log10 normalizada",["g","r"])
	cnorm = mcol.Normalize(vmin=minimo,vmax=maximo)
	cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
	celdasresiduos=0
	conceldas=0
	residuosX=[]
	residuosY=[]
	residuolenIAC=[]
	residuolenRef=[]
	residuocelda=[]
	CONTEOMAXCELDAS=0

	conteoInferior=0
	conteointermedio=0
	conteosuperior=0
	numero_Celda=np.linspace(1,(len(Xcell)-1)**2,(len(Xcell)-1)**2) 

	for i in range(len(Ycell)-1):
		for j in range(len(Xcell)-1):
			if len(infoceldas[conceldas])!=0 or len(infoceldas2[conceldas])!=0:
				CONTEOMAXCELDAS+=1
				if np.absolute(len(infoceldas[conceldas])-len(infoceldas2[conceldas]) )==0:
					if np.log10(np.absolute(len(infoceldas[conceldas]) ))<=0.5:
						conteoInferior+=1

					elif np.log10(np.absolute(len(infoceldas[conceldas])))>0.5:
						if np.log10(np.absolute(len(infoceldas[conceldas]) ))<=1:
							conteointermedio+=1
						else:
							conteosuperior+=1
				else: 
					if len(infoceldas[conceldas])==0:
						if np.absolute(np.log10(len(infoceldas2[conceldas]) ))<=0.5:
							conteoInferior+=1

						if np.absolute(np.log10(len(infoceldas2[conceldas])))>0.5:
							if np.absolute(np.log10(len(infoceldas2[conceldas])))<=1:
								conteointermedio+=1
							else:
								conteosuperior+=1

					elif len(infoceldas2[conceldas])==0:
						if np.absolute(np.log10(len(infoceldas[conceldas]) ))<=0.5:
							conteoInferior+=1
						if np.absolute(np.log10(len(infoceldas[conceldas])))>0.5:
							if np.absolute(np.log10(len(infoceldas[conceldas])))<=1:
								conteointermedio+=1
							else:
								conteosuperior+=1

					elif np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas]) ))<=0.5:
						conteoInferior+=1
					elif np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))>0.5:
						if np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))<=1:
							conteointermedio+=1
						else:
							conteosuperior+=1

			conceldas+=1
	print('Conteo de celdas: {}'.format(CONTEOMAXCELDAS))
	print('Numero de celdas intervalo inferior: {}, intervalo intermedio: {}, superior: {}'.format(conteoInferior,conteointermedio,conteosuperior))
	pesoinferior=0.5
	pesointermedio=0.75
	pesosuperior=1
	conceldas=0
	celdasresiduos=0
	CONTEOMAXCELDAS=0

	condicionj=[];condicioni=[]

	for i in range(len(Ycell)-1):
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
		for j in range(len(Xcell)-1):

			width=np.absolute(Xcell[j+1]-Xcell[j])
			if i==len(Ycell)-1:
				height=np.absolute(Ycell[i]-Ycell[i-1])
				conceldas=conceldas-1
			else:
				height=np.absolute(Ycell[i]-Ycell[i+1])

		
			
			if len(infoceldas[conceldas])==0 and len(infoceldas2[conceldas])==0:
					rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='green' )	
			elif np.absolute(len(infoceldas[conceldas])-len(infoceldas2[conceldas]))==0:
				rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='green' )
				CONTEOMAXCELDAS+=1

			elif np.log10(np.absolute(len(infoceldas[conceldas])-len(infoceldas2[conceldas])))==0:
				rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='green' )
				CONTEOMAXCELDAS+=1
	
			elif len(infoceldas[conceldas])!=0 and len(infoceldas2[conceldas])!=0 and np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))==0:
				rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='green' )		
				CONTEOMAXCELDAS+=1
			else:
				if len(infoceldas[conceldas])==0 or len(infoceldas2[conceldas])==0:
					if len(infoceldas[conceldas])==0:
						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas2[conceldas])))))
						if np.absolute(np.log10(len(infoceldas2[conceldas]) ))<=0.5:
							celdasresiduos+=1*pesoinferior
						if np.absolute(np.log10(len(infoceldas2[conceldas])))>0.5:
							if np.absolute(np.log10(len(infoceldas2[conceldas])))<=1:
								celdasresiduos+=1*pesointermedio
							else:
								celdasresiduos+=1*pesosuperior
					if len(infoceldas2[conceldas])==0:
						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas[conceldas])))))
						if np.absolute(np.log10(len(infoceldas[conceldas]) ))<=0.5:
							celdasresiduos+=1*pesoinferior
						if np.absolute(np.log10(len(infoceldas[conceldas])))>0.5:
							if np.absolute(np.log10(len(infoceldas[conceldas])))<=1:
								celdasresiduos+=1*pesointermedio
							else:
								celdasresiduos+=1*pesosuperior

					residuosY.append(Ycell[i])
					residuosX.append(Xcell[j])
					residuolenRef.append(len(infoceldas2[conceldas]))
					residuolenIAC.append(len(infoceldas[conceldas]))
					residuocelda.append(numero_Celda[conceldas])
					CONTEOMAXCELDAS+=1

					
				else:
					rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))))
					residuosY.append(Ycell[i])
					residuosX.append(Xcell[j])
					residuolenRef.append(np.log10(len(infoceldas2[conceldas])))
					residuolenIAC.append(np.log10(len(infoceldas[conceldas])))
					residuocelda.append(numero_Celda[conceldas])
					
					if np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))<=0.5:
						celdasresiduos+=1*pesoinferior
					if np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))>0.5:
						if np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))<=1:
							celdasresiduos+=1*pesointermedio
						else:
							celdasresiduos+=1*pesosuperior

					CONTEOMAXCELDAS+=1


			conceldas+=1
			ax.add_patch(rect)

	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Residual of the Synthetic CMDs \'mocks\' ',fontsize=20)
	ax.set_ylim(max(ylim),min(ylim))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)
	plt.colorbar(cpick,label="Cantidad de puntos");

	plt.savefig('Mallado.png')
	plt.close()
	Progress.finish()

	return(pesosuperior,pesointermedio,pesoinferior,np.array(residuosX),np.array(residuosY),np.array(residuolenIAC),np.array(residuolenRef),np.array(residuocelda),celdasresiduos,CONTEOMAXCELDAS)

def postprocesado(pesosuperior,pesointermedio,pesoinferior,Xcell,Ycell,ylim,xlim,minimo,maximo,residuosX,residuosY,residuoIAC,residuoRef,rescelda,infoceldas,infoceldas2,n_celdas):
	Progress = ChargingBar('Post-Processing:', max=len(Ycell)-1)

	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')

	cm1 = mcol.LinearSegmentedColormap.from_list("Cantidad de puntos. Escala log10 normalizada",["g","r"])
	cnorm = mcol.Normalize(vmin=minimo,vmax=maximo)
	cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
	conceldas=0
	numero_Celda=np.linspace(1,(len(Xcell)-1)**2,(len(Xcell)-1)**2) 
	residuo=0
	n_celdas=n_celdas**(1/2)

	for i in range(len(Ycell)-1):
		time.sleep(random.uniform(0, 0.2))
		Progress.next()
		for j in range(len(Xcell)-1):			
			width=np.absolute(Xcell[j+1]-Xcell[j])
			if i==len(Ycell)-1:
				height=np.absolute(Ycell[i]-Ycell[i-1])
				conceldas=conceldas-1
			else:
				height=np.absolute(Ycell[i]-Ycell[i+1])
			if numero_Celda[conceldas] in rescelda:
				N=numero_Celda[conceldas]

				if len(infoceldas[conceldas])!=0 and len(infoceldas2[conceldas])!=0:
					Valor=np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))
				elif len(infoceldas[conceldas])==0:
					Valor=np.absolute(np.log10(len(infoceldas2[conceldas])))
				elif len(infoceldas2[conceldas])==0:
					Valor=np.absolute(np.log10(len(infoceldas[conceldas])))

				if Valor<=0.5:
					if N+1 in rescelda and N-1 in rescelda and N+n_celdas in rescelda and N-n_celdas in rescelda:
						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='white' )	
					elif N+1 in rescelda or N-1 in rescelda or (N+1 in rescelda and N-1 in rescelda):
						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='white' )	
					elif  N+n_celdas in rescelda or N-n_celdas in rescelda:
						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='white' )	
					else:
						if len(infoceldas[conceldas])==0:
							rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas2[conceldas])))))
							#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		

						elif len(infoceldas2[conceldas])==0:
							#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		

							rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas[conceldas])))))
						else:
							rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))))		
							#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		
						if Valor<=0.5:
							residuo+=1*pesoinferior
						if Valor>0.5:
							if Valor<=1:
								residuo+=1*pesointermedio
							else:
								residuo+=1*pesosuperior
				else:
					if len(infoceldas[conceldas])==0:
						#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		

						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas2[conceldas])))))
					elif len(infoceldas2[conceldas])==0:
						#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		

						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas[conceldas])))))
					else:
						#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		

						rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color=cpick.to_rgba(np.absolute(np.log10(len(infoceldas[conceldas]))-np.log10(len(infoceldas2[conceldas])))))							#rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height,color='red')		
					
					if Valor<=0.5:
						residuo+=1*pesoinferior
					if Valor>0.5:
						if Valor<=1:
							residuo+=1*pesointermedio
						else:
							residuo+=1*pesosuperior
				
			else:
				rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='green' )	


			ax.add_patch(rect)
			conceldas+=1
	Progress.finish()

	plt.plot([],[],color='white',markersize=10,label='Post-Processing')
	plt.plot([],[],color='red',markersize=10,label='Unadjusted')

	plt.legend()
	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Post-Processing. Residual of the Synthetic CMDs \'mocks\' ',fontsize=20)
	ax.set_ylim(max(ylim),min(ylim))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)
	plt.colorbar(cpick,label="Cantidad de puntos");

	plt.savefig('Post_Mallado.png')
	plt.close()
	return(residuo)



def plotmallado_one(Xcell,Ycell,ylim,xlim,infoceldas,minimo,maximo,name):
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')

	cm1 = mcol.LinearSegmentedColormap.from_list("Cantidad de puntos",["g","r"])
	cnorm = mcol.Normalize(vmin=minimo,vmax=maximo)
	cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)

	conceldas=0
	celdasocupadas=0
	conteodedispersion=0
	for i in range(len(Ycell)-1):
		for j in range(len(Xcell)-1):
			
			width=np.absolute(Xcell[j+1]-Xcell[j])
			if i==len(Ycell)-1:
				height=np.absolute(Ycell[i]-Ycell[i-1])
				conceldas=conceldas-1
			else:
				height=np.absolute(Ycell[i]-Ycell[i+1])
			if len(infoceldas[conceldas])==0:
				rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,alpha=0.2,color='green')
			else:
				Valor1=np.log10(np.absolute(len(infoceldas[conceldas])))
				if Valor1<0.5:
					conteodedispersion+=1
				rect=matplotlib.patches.Rectangle((Xcell[j],Ycell[i]), width, height ,color=cpick.to_rgba(np.log10(len(infoceldas[conceldas]))))
				celdasocupadas+=1
			conceldas+=1
			ax.add_patch(rect)


	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Synthetic CMD \'mock\' ',fontsize=20)
	ax.set_ylim(max(ylim),min(ylim))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)
	plt.colorbar(cpick,label="Cantidad de puntos");

	plt.savefig('Mallado_'+name+'.png')
	plt.close()
	return(celdasocupadas,conteodedispersion)

def empaquetado(data,xlimits,ylimits):
	bufceldas={}; cellcount=0; maxlon=0
	lon=len(ylimits)-1
	for i in range(lon):
		for j in range(lon):

			bufceldas[cellcount]=data.loc[  (data['Color']>xlimits[j]) &  (data['Color']<xlimits[j+1]) & (data['I']<ylimits[i]) & (data['I']>ylimits[i+1]) ]
			buflon=len(bufceldas[cellcount])
			cellcount+=1

			if buflon<maxlon:
				maxlon=maxlon
			else: 
				maxlon=buflon
	return(bufceldas,maxlon,cellcount)

def mass(color1,y1,MasaFinal,MasaInicial,name,mod='inicial'):
	if mod=='inicial':
		mass=MasaInicial
		label='Masa Inicial'
	else:
		mass=MasaFinal
		label='Masa final'


	cm1 = mcol.LinearSegmentedColormap.from_list("Cantidad de puntos",["cyan","m"])
	cnorm = mcol.Normalize(vmin=min(mass),vmax=max(mass))
	cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
		
	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')
	

	
	plt.plot(color1.loc[mass<=2],y1.loc[mass<=2],'o',color='cyan',markersize=0.2)
	plt.plot(color1.loc[(mass>2) & (mass<=7)],y1.loc[(mass>2) & (mass<=7)],'o',color='white',markersize=0.2)
	plt.plot(color1.loc[mass>7],y1.loc[mass>7],'o',color='magenta',markersize=0.2)
	
	plt.plot([],[],color='cyan',markersize=12,label=label+'<2M$_\odot$')
	plt.plot([],[],color='white',markersize=12,label='2M$_\odot$<'+label+'<7 M$_\odot$')
	plt.plot([],[],color='magenta',markersize=12,label=label+'>7M$_\odot$')
	
	plt.colorbar(cpick,label="Masa en unidades M$_\odot$");


	plt.legend()
	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Synthetic CMD \'mock\' ',fontsize=20)
	ax.set_ylim(max(y1),min(y1))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)

	plt.savefig(name+'.png')
	plt.close()

def age(color1,y1,Age,name):

	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')
	Age=Age/1e09
	plt.plot(color1.loc[Age<=0.5],y1.loc[Age<=0.5],'o',color='magenta',markersize=0.2)
	plt.plot(color1.loc[(Age>0.5) & (Age<=8.9)],y1.loc[(Age>0.5) & (Age<=8.9)],'o',color='white',markersize=0.2)
	plt.plot(color1.loc[Age>8.9],y1.loc[Age>8.9],'o',color='red',markersize=0.2)
	
	plt.plot([],[],color='magenta',markersize=12,label='Edad <0.5Gyr')
	plt.plot([],[],color='white',markersize=12,label='0.5< Edad <8.9 Gyr')
	plt.plot([],[],color='red',markersize=12,label='Edad >8.9 Gyr')


	plt.legend()
	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Synthetic CMD \'mock\' ',fontsize=20)
	ax.set_ylim(max(y1),min(y1))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)

	plt.savefig(name+'.png')
	plt.close()

def T(color1,y1,T,name):

	plot=plt.figure(figsize=(13.0, 10.0))
	ax=plot.add_subplot(111)
	plt.style.use('dark_background')
	Temp=np.linspace(3.8,max(T),7)
	color=['red','yellow','white','green','orange','magenta','cyan']; c=0
	for i in Temp:
		if c==0:
			plt.plot(color1.loc[T<=i],y1.loc[T<=i],'o',color=color[c],markersize=0.2)
			plt.plot([],[],color=color[c],markersize=12,label='log(T)< '+str(round(i,2)))
		else:
			plt.plot(color1.loc[(T>=buf) & (T<=i)],y1.loc[(T>=buf) & (T<=i)],'o',color=color[c],markersize=0.2)
			plt.plot([],[],color=color[c],markersize=12,label=str(round(buf,2))+'<log(T)< '+str(round(i,2)))
		buf=i
		c+=1


	plt.legend()
	plt.xlabel('m$_{F475W}$-m$_{F814W}$', fontsize=20);plt.ylabel('m$_{F814W}$', fontsize=20)
	plt.title('Synthetic CMD \'mock\' ',fontsize=20)
	ax.set_ylim(max(y1),min(y1))
	ax.set_xlim(-0.31099999999999994,2)
	ax.set_ylim(4,-4)

	plt.savefig(name+'.png')
	plt.close()

