class operation:
    def __init__(self) -> None:
        self.m_precedence = -1
    def symbol(self):
        return None
    def calc(self,*arg)->float:
        raise Exception("not implemened")
    def set_precedence(self,i:int):
        self.m_precedence = i

class Add(operation):
    def __init__(self) -> None:
        self.m_precedence = 1
    def symbol(self):
        return "+"
    def calc(self,*arg) -> float:
        if len(arg)==2:
            return arg[0]+arg[1]
        else:
            raise Exception("to many params for add")

class Subtract(operation):
    def __init__(self) -> None:
        self.m_precedence = 1
    def symbol(self):
        return "-"
    def calc(self,*arg) -> float:
        if len(arg)==2:
            return arg[0]-arg[1]
        else:
            raise Exception("to many params for subtract")

class Multiply(operation):
    def __init__(self) -> None:
        self.m_precedence = 2
    def symbol(self):
        return "*"
    def calc(self,*arg) -> float:
        if len(arg)==2:
            return arg[0]*arg[1]
        else:
            raise Exception("to many params for multiply")

class Divide(operation):
    def __init__(self) -> None:
        self.m_precedence = 2
    def symbol(self):
        return "/"
    def calc(self,*arg) -> float:
        if len(arg)==2:
            if arg[1]==0:
                raise Exception("Division by zero")
            return arg[0]/arg[1]
        else:
            raise Exception("to many params for subtract")

if __name__ == "__main__":
    tmp = Add()
    print(tmp.m_precedence)