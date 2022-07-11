## INTRODUCTION
    
    
응용 프로그램들은 종종 INSERT, SEARCH, DELETE와 같은 사전적 작업을 지원하는 동적 집합을 필요로 한다.
해시 테이블은 사전을 구현하는 효율적인 자료구조이다. 
연결리스트에서 원소를 찾는 것은 최악의 경우 Big-θ(n) 시간이 걸린다. 
하지만 실제로 해싱은 성능이 탁월하다. 합리적인 가정 하에서 해시 테이블에서 원소를 찾는 데 걸리는 평균 수행시간은 Big-O(1)이다. 
해시 테이블은 단순한 표현인 배열을 일반화한다. 일반적인 배열에 대한 직접 주소화 방법은 배열의 임의의 위치를 O(1)에 접근하게 하는 효율적인 방법이다. 
해시 테이블은 실제 저장된 키의 개수에 비례하는 크기를 가지는 배열을 사용한다. 
실제 저장된 키의 개수가 가능한 키의 전체 개수보다 상대적으로 작은 경우 일반 배열에 직접 주소화 방법을 사용하는 것보다 효율적이다. 

![다운로드 (1)](https://user-images.githubusercontent.com/71515744/178233757-ebc46fe9-963b-4fda-8d1d-2a118e700fc5.png)
    
    
## CONCEPTION

HASH FUNCTION 종류
    
1. Division Method: 나눗셈을 이용하는 방법으로 입력값을 테이블의 크기로 나누어 계산한다. 
테이블의 크기를 소수로 정하고 2의 제곱수와 먼 값을 사용해야 효과가 좋음
      
2. Digit Folding: 각 key의 문자열을 ASCII 코드로 바꾸고 값을 합한 데이터를 테이블 내의 주소로 사용하는 방법이다.
    
3. Multiplication Method: 숫자로 된 Key값 K와 0과 1사이의 실수 A, 보통 2의 제곱수인 m을 사용하여 다음과 같은 계산을 해준다.
        
4. Universal Hashing: 다수의 해시함수를 만들어 집합 H에 넣어두고, 무작위로 해시함수를 선택해 해시값을 만드는 기법이다.
    
    
### HASH 충돌
    
만약 동일 키에 같은 해시값이 나오는 겨 ㅇ우 충돌이 일어난다. 해당 문제를 해결하기 위해서 분리 연결법(Seperate Chaning)과 개방 주소법(Open Addressing)으로 
두개로 나누어진다. 
    
<분리 연결법(Seperate Chaining)>
    
![다운로드 (2)](https://user-images.githubusercontent.com/71515744/178233858-888faf5d-cd04-462d-b67b-2e29b707080a.png)
    
Seperate Chaining: 동일한 버킷의 데이터에 대해 자료구조를 활용해 추가 메모리 사용하여 다음 데이터의 주소를 저장.
해시 테이블의 확장이 필요없고 간단하게 구현 가능하고 쉽게 삭제 가능. 단 데이터가 많아지면 동일한 버킷에 chaining되는 데이터가 많아짐
캐시 효율성 감소.
    
    
<개방 주소법(Open Addressing)>
    
    
Open Addressing: 추가적인 메모리를 사용하지 않고 비워져 있는 해시 테이블 공간을 사용.
    
* 구현 방법
        
* Linear Probing: 현재 버킷 index로부터 고정폭 만큼씩 이동하여 차례대로 검색 -> 비어 있는 버킷에 데이터 저장
* Quadratic Probing: 해시의 저장순서 폭을 제곱으로 저장. 충돌 발생시 1만큼 이동 또 충돌 2^2 3^2 씩 옮김
* Double Hashing Probing: 해시된 값을 한번 더 해싱하여 해시의 규칙성을 없애버리는 방식. 해싱된 값을 한번더 해싱하여 새로운 주소 할당. 더 많은 연산 
    
![다운로드](https://user-images.githubusercontent.com/71515744/178233864-435c0d81-07e5-4cd4-90e2-7c6c241256a1.png)
    
    
    
    
    
    
    
Refer: https://mangkyu.tistory.com/102
