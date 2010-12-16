#include <stdio.h>
int main()
{
  double a, b, c;
  a = 1; b = 10.0; c = a/b;
  if (c == 0.1) {
    printf("c == 0.1\n");
  }
  if (c == 1/10.0) {
    printf("c == 1/10.0\n");
  }
  if (c == a/b) {
    printf("c == a/b\n");
  }
}

