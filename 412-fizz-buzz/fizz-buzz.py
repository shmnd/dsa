class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            s = ''
            
            if i%3 ==0:
                s = 'Fizz'
            if i%5 ==0:
                s = 'Buzz'

            if i%3==0 and i%5==0:
                s = 'FizzBuzz'

            result.append(s or str(i))

        return result
                

        