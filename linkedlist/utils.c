#include <stdio.h>

char *strcpy(char*s1,char*s2){
	char *str = s2;

	while(*s1 != '\0'){
		*s1 = *s2;
		s1++;
		s2++;
	}
	*s1 = '\0';
	return str;
}	

void main(){
	char s1[10];
	char s2[5] = "sri";

	printf("%s,%s",s2,strcpy(s1,s2));
	
}
