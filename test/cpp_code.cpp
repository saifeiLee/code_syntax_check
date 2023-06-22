#include <iostream>
#include <unistd.h>

// quick sort
void quick_sort(int *arr, int left, int right) {
  if (left >= right)
    return;
  int i = left, j = right, pivot = arr[left];
  while (i < j) {
    while (i < j && arr[j] >= pivot)
      j--;
    if (i < j)
      arr[i++] = arr[j];
    while (i < j && arr[i] <= pivot)
      i++;
    if (i < j)
      arr[j--] = arr[i];
  }
  arr[i] = pivot;
  quick_sort(arr, left, i - 1);
  quick_sort(arr, i + 1, right);
}

int main() {
  int arr[] = {3, 2, 1, 5, 6, 4};
  quick_sort(arr, 0, 5);
  for (int i = 0; i < 6; i++)
    std::cout << arr[i] << " ";
  std::cout << std::endl;
  std::cout << "Start sleep" << std::endl;
  sleep(600);
  return 0;
}