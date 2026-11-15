import json

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        
    def check_answer(self, user_answer):
        # 정답 확인 로직
        pass
        
    def to_dict(self):
        # JSON 저장용 딕셔너리 반환
        pass

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_data(1) # 시작할 때 데이터 불러오기/        

    # 메뉴 출력 및 분기 로직
    def run(self):
        
        while True:

            # 메뉴 출력
            print("""========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================""")

            # 사용자 입력값 검증
            try:
                usr_num=int(input("선택:").strip())

                if usr_num == 1:
                    self.play_quiz()
                elif usr_num == 2:
                    self.add_quiz()
                elif usr_num == 3:
                    self.quiz_lsit()
                elif usr_num == 4:
                    self.show_best_score()
                elif usr_num == 5:
                    print("프로그램이 종료됩니다.")
                    break
                else:
                    print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.\n")
            except:
                print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.\n")

    # 퀴즈 풀기 로직
    def play_quiz(self):
        
        # 퀴즈 불러오기
        problem_list = self.load_data(0)
        p_list = problem_list["quizzes"] # 이렇게하면 리스트 내부 딕셔너리 형태
        self.best_score = problem_list["best_score"] # 기존 최고 점수 가져오기

        score = 0 # 점수 변수

        # 퀴즈 시작
        print(f"\n\n📝 퀴즈를 시작합니다! (총 {len(p_list)}문제)")

        for p_dic in p_list:
            # 정답 입력
            while True:
                print("\n-----------------------\n")
                
                # 문제 출력
                print(p_dic["question"])
    
                # 선택지 출력
                for i in range(0, len(p_dic["choices"])):
                    print(f"{i+1}. {p_dic["choices"][i]}")

                # 사용자 입력값 검증
                try:
                    answer = int(input("정답 입력 : ").strip())

                    if answer == p_dic["answer"]:
                        print("✅ 정답입니다!")
                        score += 1
                        break
                    elif answer != p_dic["answer"] and 1 <= answer <= 4:
                        print("❎ 오답입니다ㅜ")
                        break
                    else:
                        print("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.\n")
                except:
                    print("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.\n")

                

        # 최종 점수 산출
        if score == 0:
            total_score = 0
        else:
            total_score = round(100*(float(score)/len(p_list)), 2)

        # 최종 점수 출력
        print("\n\n========================================")
        print(f"결과: {len(p_list)}문제 중 {score}문제 정답! ({total_score}점)")
        # 최종 점수가 최고 점수를 넘었을 때
        if total_score > self.best_score:
            score_info = [total_score, len(p_list), score]
            self.save_data(score_info)
            print("🎉 새로운 최고 점수입니다!")
        print("========================================\n\n")

    # 퀴즈 추가 로직
    def add_quiz(self):
        
        choices = [] # 선택지 입력을 위한 빈 리스트

        while True:
            # 사용자 입력값 검증
            try:
                print("📌 새로운 퀴즈를 추가합니다.")
                # 문제 입력
                question = input("문제를 입력하세요: ").strip()

                if question == "":
                    print("문제는 공백일 수 없습니다.\n")
                else:
                    break     
            except:
                print("\nCtrl+C는 동작하지 않습니다.\n")

        # 선택지 입력
        for i in range(0, 4):
            while True:
                # 사용자 입력값 검증
                try:
                    select = input(f"선택지 {i+1}: ").strip()

                    if select == "":
                        print("선택지는 공백일 수 없습니다.\n")
                    else:
                        choices.append(select)
                        break
                except:
                    print("\nCtrl+C는 동작하지 않습니다.\n")

        # 정답 입력
        while True:
            # 사용자 입력값 검증
            try:
                correct = int(input("정답 번호 (1-4): ").strip())

                if 1 <= correct <= 4:
                    break
                else:
                    print("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.\n")
            except:
                print("잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.\n")

        self.save_data(question, choices, correct)

        print("✅ 퀴즈가 추가되었습니다!")

    # 퀴즈 리스트 로직
    def quiz_lsit(self):

         # 퀴즈 불러오기
        problem_list = self.load_data(0)
        p_list = problem_list["quizzes"] # 이렇게하면 리스트 내부 딕셔너리 형태
        
        print(f"📋 등록된 퀴즈 목록 (총 {len(p_list)}개)")
        print("\n\n-----------------------")

        for i, (p_dic) in enumerate(p_list):
            print(f"[{i+1}] {p_dic["question"]}")
        print("-----------------------\n\n")
    
    # 최고 점수 확인 로직
    def show_best_score(self):
        show_best_score = self.load_data(0)["best_score"] # 기존 최고 점수
        show_question_number = self.load_data(0)["question_number"] # 최고 점수였을 때 문제 수
        show_correct_number = self.load_data(0)["correct_number"] # 최고 점수였을 때 맞춘 수

        print(f"\n🏆 최고 점수: {show_best_score}점 ({show_question_number}문제 중 {show_correct_number}문제 정답)\n")

    # state.json에 저장된 데이터 불러오기 로직
    def load_data(self, *args):

        if args[0] == 1:
            # state.json 유/무 체크 및 파일 손상 여부 체크
            try:
                with open("state.json", "r", encoding="utf-8") as f:
                    check = json.load(f)
                    print("JSON 파일에 아무런 문제도 발견되지 않았습니다.")
            except FileNotFoundError:
                print("JSON 파일이 존재하지 않아 기본값으로 초기화합니다.")

                with open("basic_state.json", "r", encoding="utf-8") as f:
                    basic = json.load(f)
                with open("state.json", "w", encoding="utf-8") as f:
                    json.dump(basic, f, ensure_ascii=False, indent=4)
            except json.JSONDecodeError:
                print("JSON 파일의 문법이 손상되었습니다. 기본값으로 초기화합니다.")

                with open("basic_state.json", "r", encoding="utf-8") as f:
                    basic = json.load(f)
                with open("state.json", "w", encoding="utf-8") as f:
                    json.dump(basic, f, ensure_ascii=False, indent=4)

            with open("state.json", "r", encoding="utf-8") as f:
                            file_data = json.load(f)
            
            return file_data
        else:
            with open("state.json", "r", encoding="utf-8") as f:
                file_data = json.load(f)

            return file_data
        

    # state.json에 저장 로직
    def save_data(self, *args):

        # 문제, 선택지, 정답 json에 추가
        if len(args) == 3:
            # json 데이터 내부 리스트에 포함될 딕셔너리 생성
            data = \
            {
                "question": args[0],
                "choices": args[1],
                "answer": args[2]
            }

            # json 데이터 불러오기
            try:
                with open("state.json", "r", encoding="utf-8") as f:
                    file_data = json.load(f)
            except FileNotFoundError:
                file_data = {"quizzes": [], "best_score": 0}

            # json 데이터 내부 리스트에 딕셔너리 추가 
            file_data["quizzes"].append(data)

            # 다시 json 데이터 쓰기
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(file_data, f, ensure_ascii=False, indent=4)
        # 최고 점수 json에 추가        
        else:
            # json 데이터 불러오기
            try:
                with open("state.json", "r", encoding="utf-8") as f:
                    file_data = json.load(f)
            except FileNotFoundError:
                file_data = {"quizzes": [], "best_score": 0}

            # json 데이터 내부 best_score 키에 해당하는 값에 최고점수 대입 
            file_data["best_score"] = args[0][0]
            
            file_data["question_number"] = args[0][1]

            file_data["correct_number"] = args[0][2]

            # 다시 json 데이터 쓰기
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(file_data, f, ensure_ascii=False, indent=4)


# 실제 실행 부분
if __name__ == "__main__":
    game = QuizGame()
    game.run()