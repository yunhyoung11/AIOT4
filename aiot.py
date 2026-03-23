from gpiozero import LED    #gpipzero 라이브러리로부터 'LED' 함수를 받아옴
from time import sleep      #time 라이브러리로부터 'sleep' 함수를 받아옴 

carLedRed = 2               #LED 핀 번호를 위 숫자들로 정의 
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

carLedRed = LED(2)           #LED를 클래스의 객체로 초기화,핀 번호로 객체를 생성 
carLedYellow = LED(3)        
carLedGreen = LED(4)         
humanLedRed = LED(20)        
humanLedGreen = LED(21)      

try:
    while 1:                      #무한반복 (신호등이 계속 돌아가게 만들어줌)
        carLedRed.value = 0       #자동차 빨간불 꺼짐 
        carLedYellow.value = 0    #자동차 노란불 꺼짐 
        carLedGreen.value = 1     #자동차 초록불 켜짐 
        humanLedRed.value = 1     #보행자 빨간불 켜짐 
        humanLedGreen.value = 0   #보행자 초록불 꺼짐 
        sleep(3.0)                #3초동안 유지 위 동작들을 반복 
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)
    
except KeyboardInterrupt:           #ctrl c를 누르기 전까지 코드를 실행하는 예외 처리 블록 
    pass                            #ctrl c를 누르면 실행 종료 

carLedRed.value = 0                 #종료 시 LED꺼짐   
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0
