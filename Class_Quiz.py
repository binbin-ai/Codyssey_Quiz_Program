import sys

class Quiz_Solve:

    def Quiz_go(self):
        
        sum = 0

        print("\n퀴즈를 시작합니다!")
        
        problem_arr = \
        {
            3:"마블 시네마틱 유니버스에서 타노스가 모은 인피니티 스톤의 개수는?\n1. 4개\n2. 5개\n3. 6개\n4. 7개",
            1:"유재석의 나이는?\n1. 54살\n2. 53살\n3. 52살\n4. 51살"
        }

        for i, (correct, problem) in enumerate(problem_arr.items()):
            print("\n-----------------------\n")
            torf = self.Quiz_ing(i+1, problem, correct)
            sum += torf

        print("\n\n========================================")
        print(f"결과: 2문제 중 {sum}문제 정답!")
        print("========================================")

    def Quiz_ing(self, pb_num, pb, correct):
    
        print(f"[문제 {pb_num}]")
        print(pb)
        
        check = 0
        
        while(1):
            if(check == 1):
                break
            try:
                answer = int(input("\n정답 입력: "))
                while(1):
                    if(answer == correct):
                        print("정답입니다!")
                        print("\n-----------------------\n")
                        check = 1
                        return 1
                    elif(answer != correct and 1 <= answer <= 4):
                        print("오답입니다ㅜ")
                        print("\n-----------------------\n")
                        check = 1
                        return 0   
                    else:
                        print("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.\n")
                        break
            except:
                print("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.\n")


print("""========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기 ///
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================""")

while(1):
    try:
        usr_num=int(input("선택:"))
        break
    except:
        print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.\n")

if usr_num == 1:
    Quiz_Solve_Object = Quiz_Solve()
    Quiz_Solve_Object.Quiz_go()
elif usr_num == 5:
    print("프로그램이 종료됩니다.")
    sys.exit()
elif usr_num == 2 or usr_num == 3 or usr_num == 4:
    print("\n아직 미구현된 옵션입니다.\n")
else:
    print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.\n")