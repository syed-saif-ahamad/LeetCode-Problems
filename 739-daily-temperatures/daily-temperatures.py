class Solution:
    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperature)
        for i in range(len(temperature)):
            while stack and temperature[i] > temperature[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer