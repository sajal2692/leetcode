class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                a = record.pop()
                b = record[-1]
                record.append(a)
                record.append(a+b)
            elif op == "D":
                a = record[-1]
                record.append(2*a)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
        