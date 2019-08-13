class Solution:

  def reverseWords(self, inputStr):
    inputStr = inputStr.strip()
    reversedStr = ''
    words = []

    word = ''
    for char in inputStr:
      if char != ' ':
        word += char
      else:
        words.append(word)
        word = ''
    words.append(word)

    for i in range(len(words) - 1, 0, -1):
      reversedStr = reversedStr + words[i] + ' '
    reversedStr += words[0]

    return reversedStr


inputStr = "fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq"
s = Solution()
print(s.reverseWords(inputStr))
