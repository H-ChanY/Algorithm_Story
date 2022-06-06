# 퀵 정렬


## 퀵 정렬이란

    * 불안정 정렬에 속하며, 다른 원소와의 비교만으로 정렬을 수행하는 비교 정렬이다.
    * 분할 정복 알고리즘의 하나, 매우 빠른 수행 속도를 자랑. 

## 퀵 정렬 과정

    1. 리스트 안에 있는 한 요소를 선택, 해당 원소는 피벗이라고 함. 
    2. 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗 왼쪽으로 옮겨지고 큰 요소들은 오른쪽으로 옮겨짐. 
    3. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬.
        * 분할된 부분 리스트에 대하여 순환 호출을 이용하여 정렬을 반복.
        * 부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개 부분 리스트로 나누는 과정을 반복.
    4. 부분 리스트들이 더 이상 분할이 불가능할 때가지 반복. 
    
![quick-sort](https://user-images.githubusercontent.com/71515744/170242364-3829870e-0779-42b3-be3a-905e7e152935.png)

![quick-sort2](https://user-images.githubusercontent.com/71515744/170242686-a4225ba8-ce68-4e2f-912f-865fbfe23dea.png)


```
# include <stdio.h>
# define MAX_SIZE 9
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

// 1. 피벗을 기준으로 2개의 부분 리스트로 나눈다.
// 2. 피벗보다 작은 값은 모두 왼쪽 부분 리스트로, 큰 값은 오른쪽 부분 리스트로 옮긴다.
/* 2개의 비균등 배열 list[left...pivot-1]와 list[pivot+1...right]의 합병 과정 */
/* (실제로 숫자들이 정렬되는 과정) */
int partition(int list[], int left, int right){
  int pivot, temp;
  int low, high;

  low = left;
  high = right + 1;
  pivot = list[left]; // 정렬할 리스트의 가장 왼쪽 데이터를 피벗으로 선택(임의의 값을 피벗으로 선택)

  /* low와 high가 교차할 때까지 반복(low<high) */
  do{
    /* list[low]가 피벗보다 작으면 계속 low를 증가 */
    do {
      low++; // low는 left+1 에서 시작
    } while (low<=right && list[low]<pivot);

    /* list[high]가 피벗보다 크면 계속 high를 감소 */
    do {
      high--; //high는 right 에서 시작
    } while (high>=left && list[high]>pivot);

    // 만약 low와 high가 교차하지 않았으면 list[low]를 list[high] 교환
    if(low<high){
      SWAP(list[low], list[high], temp);
    }
  } while (low<high);

  // low와 high가 교차했으면 반복문을 빠져나와 list[left]와 list[high]를 교환
  SWAP(list[left], list[high], temp);

  // 피벗의 위치인 high를 반환
  return high;
}

// 퀵 정렬
void quick_sort(int list[], int left, int right){

  /* 정렬할 범위가 2개 이상의 데이터이면(리스트의 크기가 0이나 1이 아니면) */
  if(left<right){
    // partition 함수를 호출하여 피벗을 기준으로 리스트를 비균등 분할 -분할(Divide)
    int q = partition(list, left, right); // q: 피벗의 위치

    // 피벗은 제외한 2개의 부분 리스트를 대상으로 순환 호출
    quick_sort(list, left, q-1); // (left ~ 피벗 바로 앞) 앞쪽 부분 리스트 정렬 -정복(Conquer)
    quick_sort(list, q+1, right); // (피벗 바로 뒤 ~ right) 뒤쪽 부분 리스트 정렬 -정복(Conquer)
  }

}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[n] = {5, 3, 8, 4, 9, 1, 6, 2, 7};

  // 퀵 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 8)
  quick_sort(list, 0, n-1);

  // 정렬 결과 출력
  for(i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}
https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html
```


## 퀵 정렬 특징

    * 장점
        1. 속도가 빠름 O(nlog n)
        2. 추가 메모리 공간을 필요로 하지 않는다. 
    
    * 단점
        1. 정렬된 리스트에 대해서는 퀵 정렬의 불균형 분할에 의해 오히려 수행시간이 더 많이 걸림.
  
    * 특징 
        1. 일정하게 분할 되면 시간 복잡도가 O(nlog n)이다.  
  
## 의사 결정 코드
  
```  
QUICKSORT(A,p,r)
      q= partiton(A,p,r)
      QUICKSORT(A,p,q-1)
      QUICKSORT(A,q-1,r)
        
PARTITION(A,p,r)
x=A[r]
i=p-1
for j=p to r-1
      if A[j]<=x
            i=i+1
            exchange A[i] with A[j]
exchange A[i+1] with A[r]
return i+1
```

## 평균적인 경우
  
    모든 입력이 똑같은 확률로 발생한다고 가정.
    하지만 그렇지 않음. 
    그래서 랜덤화 기법으로 성능의 기댓값을 높일 수 있다. 
    
    
