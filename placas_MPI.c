#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

int main(){

  int world_size, rank, source, destination;
  MPI_Request send_request, recv_request;
  MPI_Status status;

  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &world_size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  float L = 5, l = 2, d = 1, h = 0.02, V0 = 100, N = 64;
  int n = (int)(L/h);

  
  //inicializa la matriz
  int i, j, k;
  int z=n/world_size;
  int first_col=z*rank-1;
  int primera_placa=(int)((L/2-d/2)/h)-first_col;
  int segunda_placa=(int)((L/2+d/2)/h)-first_col;
  if(rank==0)
	{
	double **matriz;
  	matriz = (double**) malloc(n*sizeof(double*));

	int m=(n/world_size+1);
  	for (i=0; i<=n; i++){
    	matriz[i] = (double*) malloc(m*sizeof(double));
  	}
	
	for(i=0; i<n; i++){
   		 for(j=0; j<m; j++){
      			matriz[i][j] = 5;
    		}
	}
	//inicializa las fronteras verticales
  	for(i=0; i<n; i++){
    		matriz[i][0] = 0;
  	}
	
	//inicializa las fronteras horizontales
  	for(j=0; j<m; j++){
    		matriz[0][j] = 0;
    		matriz[n-1][j] = 0;
 	 }
	//incluye primera placa
	if(m>=(int)((L/2-d/2)/h))
	{
		for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
   			matriz[i][(int)((L/2-d/2)/h)] = -V0/2;
  		}
	}
	//incluye segunda placa
	if(m>=(int)((L/2+d/2)/h))
	{
		for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
   			matriz[i][(int)((L/2+d/2)/h)] = V0/2;
  		}
	}

	printf("procesador # %d",rank);
	  for(i=0; i<n; i++){
    		for(j=0; j<m; j++){
      			printf("%f |", matriz[i][j]);
    		}
		printf("\n");
  		}


	}
  else if(rank==world_size-1)
    {
      
      double **matriz;
  	matriz = (double**) malloc(n*sizeof(double*));
	
	int m=(n/world_size+1);
  	for (i=0; i<=n; i++){
    	matriz[i] = (double*) malloc(m*sizeof(double));
  	}
	
	for(i=0; i<n; i++){
   		 for(j=0; j<m; j++){
      			matriz[i][j] = 5;
    		}
	}

	//inicializa las fronteras horizontales
  	for(j=0; j<m; j++){
    		matriz[0][j] = 0;
    		matriz[n-1][j] = 0;
 	 }

	//inicializa las fronteras verticales
  	for(i=0; i<n; i++){
    		matriz[i][m-1] = 0;
  	}

	//incluye primera placa
	if(primera_placa>=0)
	{
		for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
   			matriz[i][primera_placa] = -V0/2;
  		}
	}

	//incluye segunda placa
	if(segunda_placa>=0)
	{
		for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
   			matriz[i][segunda_placa] = -V0/2;
  		}
	}
	printf("procesador # %d",rank);
	  for(i=0; i<n; i++){
    		for(j=0; j<m; j++){
      			printf("%f ", matriz[i][j]);
    		}
		printf("\n");
  		}

    }
    else
    {
 
 	double **matriz;
  	matriz = (double**) malloc(n*sizeof(double*));
	
	int m=(n/world_size+2);
  	for (i=0; i<=n; i++){
    	matriz[i] = (double*) malloc(m*sizeof(double));
  	}
	
	for(i=0; i<n; i++){
   		 for(j=0; j<m; j++){
      			matriz[i][j] = 5;
    		}
	}

	//inicializa las fronteras horizontales
  	for(j=0; j<m; j++){
    		matriz[0][j] = 0;
    		matriz[n-1][j] = 0;
 	 }

	//incluye primera placa
	if(primera_placa>=0 && primera_placa<m)
	{
		for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
   			matriz[i][primera_placa] = -V0/2;
  		}
	}

	//incluye segunda placa
	if(segunda_placa>=0 && segunda_placa<m)
	{
		for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
   			matriz[i][segunda_placa] = -V0/2;
  		}
	}
	printf("procesador # %d",rank);
	  for(i=0; i<n; i++){
    		for(j=0; j<m; j++){
      			printf("%f ", matriz[i][j]);
    		}
		printf("\n");
  		}

    }

  /*
  //inicializa la matriz temporal
  double **matriz2;
  matriz2 = (double**) malloc(n*sizeof(double*));

  for (i=0; i<=n; i++){
    matriz2[i] = (double*) malloc(n*sizeof(double));
  }

  for(i=0; i<n; i++){
    for(j=0; j<n; j++){
      matriz2[i][j] = 0;
    }
  }

  for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
    matriz2[i][(int)((L/2-d/2)/h)] = -V0/2;
    matriz2[i][(int)((L/2+d/2)/h)] = V0/2;
  }


  //metodo de relajacion
  for(k=0; k<N; k++){
    for(i=1; i<n-1; i++){
      for(j=1; j<n-1; j++){
	  matriz2[i][j]=0.25*(matriz[i+1][j]+matriz[i][j+1]+matriz[i-1][j]+matriz[i][j-1]);
      }
    }
    for(i=(int)((L/2-l/2)/h); i<(int)((L/2+l/2)/h); i++){
      matriz2[i][(int)((L/2-d/2)/h)] = -V0/2;
      matriz2[i][(int)((L/2+d/2)/h)] = V0/2;
    }
    for(i=1; i<n-1; i++){
      for(j=1; j<n-1; j++){
	matriz[i][j] = matriz2[i][j];
      }
    }
  }

  


  //calcula el campo electrico
  double **Ex;
  Ex = (double**) malloc(n*sizeof(double*));
  double **Ey;
  Ey = (double**) malloc(n*sizeof(double*));

  for (i=0; i<=n; i++){
    Ex[i] = (double*) malloc(n*sizeof(double));
    Ey[i] = (double*) malloc(n*sizeof(double));
  }

  for(i=0; i<n; i++){
    for(j=0; j<n; j++){
      Ex[i][j]=(matriz[i][j]-matriz[i+1][j])/h;
      Ey[i][j]=-(matriz[i][j]-matriz[i][j+1])/h;
    }
  }


  //imprime los valores del potencial y del campo
  for(i=0; i<n; i++){
    for(j=0; j<n; j++){
      printf("%f\n", matriz[i][j]);
    }
  }
  
  for(i=0; i<n; i++){
    for(j=0; j<n; j++){
      printf("%f\n", Ex[i][j]);
    }
  }

  for(i=0; i<n; i++){
    for(j=0; j<n; j++){
      printf("%f\n", Ey[i][j]);
    }
  }

*/

 
 MPI_Finalize();
 return 0;
} 

