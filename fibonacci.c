#include <stdio.h>
#include <stdlib.h>
    
int fiboc(int n){

int i,fib = 1, aux = 0, j=1;
  while(fib < n)
  { 
    fib = fib + aux;                 
    aux = j;
    j = fib;  
      if (n == fib){
        printf("O numero %d pertence a sequencia do fibonacci\n", n);
	 break;
      }
      else if ( fib > n){
        printf("O numero %d não pertence a sequencia do fibonacci\n", n);                          		break;			
      }
   }
    	
}    
     
int main(){
 int n;
 printf("Informe um numero inteiro\n");
 scanf("%d", &n);
 
 fiboc(n);

 return 0;  
}
