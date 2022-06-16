1. args, kwargs를 사용하는 예제 코드 짜보기
 + args,kwargs 라고 써줄 필요는 없다. 하지만 앞에 *,** 는 꼭 붙여야한다.
+ args 는 '가변 인자' 를 위한 변수. 튜플형태로 저장한다.
```
def prac(*args):
        result = 0
        for i in args:
                result += i
        print(result)
prac(1,2,3,4,5)
```
+ kwargs 는 keyword arguments 의 약자
kwargs 딕셔너리 형태로 값을 저장한다. 또한 args 와 달리 피라미터 명을 같이 보낼 수 있다.
```
def name_and_age(**kwargs):
        print(kwargs)
name_and_age(name="하진", age="30")
name_and_age(name="바보", age="15")
```
+ 같이 사용 가능
```
def prac(*args, **kwargs):
        result = 0
        for i in args:
                result += i
        print(args,kwargs)
prac(1,2,3,4,5, name='이것은', result='kwargs입니다')
```

 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
 파이썬 객체는 수정가능합 타입이고 있고, 수정 불가능한 타입이 있다.
 수정 가능한 타입은 mutable, 불가능한 타입이 immutable 이다
 mutable - int, float, tuple, str, bool
 immutalbe - list ,dictionary 
 
 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
 관계형 데이터베이스에서 키는 릴레이션(테이블)에서 특정 투플을 식별할때 사용하는 속성 혹은 속성의 집합이다.
 즉 키가 되는 속성은 반드시 값이 달라서 투플들을 서로 구별할 수 있어야 한다.
+ PK(primary Key)
데이터베이스 테이블의 설계(데이터베이스)를 고유하게 식별하는 키
기본키는 다른 항목과 절대로 중복되어 나타날 수 없는 단일 값(unique)을 가집니다
기본키는 절대 null(아무런 값이 없는 상태) 값을 가질 수 없습니다.
(주민번호, 제품고유번호, 사용자 id등 서로 다른값을 가져야 하는것이 주요키로 사용된다.)
+ index 
주요키와 더불어 레코드를 분류할 때 사용되는 것이 인덱스 입니다.
인덱스는 데이터의 순서를 미리 정렬해서 저장할 때 사용된다.
Primakey 키도 인덱스의 일종으로서, 인덱스는 중복된 값에 대한 정렬이 가능한 반면에 주요키는 중복된 값을 가질 수 없다.
+ FK(Foreing key)
외래키는 다른 릴레이션의 기본키를 참조하는 속성을 말한다. 외래키는 다른 릴레이션의 기본키를 참조하여 관계 데이터 모델의 특징인 릴레이션 간의 관계를 표현한다.
OnoToMany,ManyToMnay,OneToOne
+ Unique
각 필드의 값이, 테이블 내에서 "유일한 값"을 가지는 필드로 만든다. 즉 모든 레코드가 서로 다른 값을 가져야만 할 때 사용된다.
모델을 정의할때 Field(unique=True)로 유니크의 값을 지정할 수 있다. 보통 타임스탬프 값이 유니크 값이 될 수 있다.
 4. django에서 queryset과 object는 어떻게 다른지 서술하기
+ QuerySet
QuerySet 은 데이터베이스에서 전달받은 객체들의 list 이다.
각 객체들은 DB에서 하나의 record(row)에 해당한다.
python 으로 작성한 코드가 SQL로 mapping 되어 QuerySet 이라는 자료형태로 넘어온다.
ORM 코드가 객체를 불러오지만 실제DB에 쿼리가 이루어지는 것은 아니다.
QuerySet 의 lazy 한 특성으로 인해 실제 데이터를 가져오기 위해서는 iterate 시켜야 한다.
객체를 object 라고 한다.
