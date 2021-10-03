#include <stdio.h>
#include <string.h>

#define LEN 10

int str_len(char *str){
  int i=0;
  while(str[i]!='\0'){
    i++;
  }
  return i;
}

int isSubString(char *s){
  return 1;
}

int* mergeSortedArray(int *a1,int *a2){
  int *t1, *t2;
  int *res=NULL;

  t1 = a1;
  t2 = a2;


return res;
}

void reverse(char *str){
  char *b,*e,tmp;
  int len = str_len(str)-1;
  int i=0;

  printf("%s\n",str);

  b = str;
  e = str + len;

  printf("%c",*e);
  for(i=0;i<=len/2;i++){
    //swap 1st and last element
   // *arr[len]

   tmp = *e;
   *e = *b;
   *b = tmp;
  printf("string length = %d\n",len);

   e--;
   b++;

   printf("%s",str);
  }

}
int binarysearch(int *arr,int n,int target){
  int l,r,mid;
  l=0;
  r=n-1;

  while(l<=r){
    mid = (l+r)/2;
    if(arr[mid]==target)
      return mid;

    if(target<arr[mid])
      r=mid-1;
    else if(target>arr[mid])
      l=mid+1;
  }
  return -1;
}


int main(void) {
  char *str = "srikanth";
  int arr1[100]={1,2,3};
  int arr2[3]={1,4,5};

  int res_len;
  int l1=(sizeof(arr1)/sizeof(int));
  res_len = (sizeof(arr1)/sizeof(int))
            + (sizeof(arr2)/sizeof(int));


  //int *res = (int*)malloc();
  //printf("%c",*(str+1));
  //reverse(&str[0]);
  //reverse(&str[0]);
  printf("%s\n",str);

  printf("%d",binarysearch(arr1,3,3));
  //res = mergeSortedArray(srt1);

  return 0;
}







#if 0

NOTES
=====


Initialization
1. char str[] = "GeeksforGeeks";
2. char str[50] = "GeeksforGeeks";
3. char str[] = {'G','e','e','k','s','f','o','r','G','e','e','k','s','\0'};
4. char str[14] = {'G','e','e','k','s','f','o','r','G','e','e','k','s','\0'};


  //In C printf(), %n is a special format specifier which instead of printing something causes printf() to load the variable pointed by the corresponding argument with a value equal to the number of characters that have been printed by printf() before the occurrence of %n.
  printf("geeks for %ngeeks ", &c);
  printf("%d", c);


 Passing array by reference

 void foo(int * x);
void foo(int x[100]);
void foo(int x[]);
void foo(int (&x)[100]);
void foo(int & x[100]); // error

Pointer Arithmetic
Adds address of the the same type
example:
char str[9]="srikanth"
printf("%c",*(str+1)) ===> "r"

#endif
