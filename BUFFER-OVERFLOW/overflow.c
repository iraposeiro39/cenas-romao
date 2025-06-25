#include <stdio.h>
#include <string.h>
 
int main(){
 
    char nome[10];
    char apelido[10];
 
 
    printf("Inserir nome: \n");
    //gets(nome);
    scanf("%s", &nome);
    printf("Escreveu o nome: %s\n",  nome);
    printf("Inserir apelido: \n");
    scanf("%s", &apelido);
    printf("Escreveu o apelido: %s\n",  apelido);
 
    printf("Posicao mem Nome: %p\n", &nome);
    printf("Posicao mem Apelido: %p\n", &apelido);
 
    return 0;
 
 
}