# 힙 소트란

## 힙이란

    힙은 우선 순위 중심으로 정렬된 시퀀스를 활용해야 할 때 유용한 자료구조이다.
    힙은 한 노드가 최대 두개의 자식 노드를 가지면서, 마지막 레벨을 제외한 모든 레벨에서 노드들이 꽉 채워진 완전이진트리이다.
 
## Heapify

주어진 자료구조에서 힙 성질을 만족하도록 하는 연산을 heapify라고 한다. 
    
![5tVTziM](https://user-images.githubusercontent.com/71515744/170421422-506c8d00-c7ec-449f-a1d8-ae73b2a3a67c.png)
    
* Max Heapify로 가정
* 부모 노드에 있는 4는 14보다 작기 때문에 왼쪽으로 온다. 
* 2보다 크고 8보다 작기 때문에 4와 8자리를 교환
* 확인할 자식노드가 없으므로 연산 종료
    
```
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]: # 왼쪽으로 가는거
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]: # 오른쪽으로 가는거 
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest] # 바뀐거 확인하고 다시 heapify해주기. 
        heapify(unsorted, largest, heap_size)
```

* heapify의 계산복잡성은 최악의 경우 루트노드에서 잎새노드까지 값을 비교해야 하므로 트리의 높이 O(h=lg n)에 의존적
* 값을 비교하거나 바꾸는 연산은 O(1)이므로 결과적으로 heapify의 계산복잡성은 O(lg n)이다.
  
## insert 

* 힙은 자료구조의 일종이므로 삽입 연산이 가능해야함. 
* 삽입을 할 때 마지막 레벨의 비어있는 제일 왼쪽 노드에 삽입 시켜줌.
* 삽입을 하면 heapify의 속성이 깨질 수 있음. 확인해서 힙 속성을 맞춰줘야함. 
* 시간 복잡도 O(lg n)
  
## delete
    
* 지우고 싶은 값이 중간에 있으면 어떻게 해야할까?
* 마지막 레벨의 마지막 인덱스에 있는 값을 지우고 싶은 노드에 넣어준다.
* 그러고 난 뒤 다시 힙 속성이 깨지지 않도록 heapify를 해준다. 

  
## Build Heap
  
* 임의의 숫자들을 최대 힙으로 구성해보자. 이러한 연산과정을 build heap이라고 한다. 
* 아래와 같은 리스트들이 있다. 
    ```
    12,30,6,7,4,13,8,11,50,24,2,5,10
    ```
* build heap 하는 가장 단순한 방법 
1. 비어있는 힙 구조에 차례로 insert 한다.
2. 마지막 요소를 insert 할 때 힙 구조를 구성하고 잇는 노드는 n-1개이다. 
3. insert의 계산 복잡도는 O(lg n)이고
4. 총 n번 반복해야하므로 n*O(lg n)이다.
  
  
