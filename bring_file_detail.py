with open('problem.txt', 'w', encoding='utf-8') as f:
    f.write("문제:마블 시네마틱 유니버스에서 타노스가 모은 인피니티 스톤의 개수는?\n1. 4개\n2. 5개\n3. 6개\n4. 7개\n\n")
    f.write("정답:3")

with open('problem.txt', 'r', encoding='utf-8') as f:
    content = f.read()

blocks = content.split('문제:')
blocks = [b for b in blocks if b.strip()]

# print(blocks[0])

if '정답:' in blocks[0]:
    parts = blocks[0].split('정답:')
    print(parts)




