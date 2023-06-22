#include <stdio.h>
#include <unistd.h>

int sum(int a, int b) { return a + b; }

// quick sort
void quick_sort(int *arr, int left, int right) {
  if (left >= right)
    return;
  int i = left, j = right, key = arr[left];
  while (i < j) {
    while (i < j && arr[j] >= key)
      j--;
    arr[i] = arr[j];
    while (i < j && arr[i] <= key)
      i++;
    arr[j] = arr[i];
  }
  arr[i] = key;
  quick_sort(arr, left, i - 1);
  quick_sort(arr, i + 1, right);
}

int main() {
  int arr[] = {1, 3, 2, 5, 4};
  quick_sort(arr, 0, 4);
  for (int i = 0; i < 5; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n Start Sleep...\n");
  sleep(600);
  return 0;
}