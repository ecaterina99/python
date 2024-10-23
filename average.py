scores=[]
for i in range(3):
      score = int(input("score: "))
      scores.append(score)
    
average = sum(scores)/len(scores)
print(f"Average is: {average}")