testscorestring = input("")
classRankString = input("")

testScore = int(testscorestring)
classRank = int(classRankString)

if testScore >= 90:
  if classRank >= 25:
      print("Accept")
  else:
      print("Reject")
else:
  if testScore >= 80:
      if classRank >= 50:
          print("Accept")
      else:
          print("Reject")
  else:
      if testScore >= 70:
          if classRank >= 75:
              print("Accept")
          else:
              print("Reject")
      else:
          print("Reject")






    