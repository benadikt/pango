import json
import os
from operations import * 
import numpy as np

class calculator:
    def __init__(self) -> None:
        #Using reflection to get the class out of app.json
        self.op_dic = {}
        self.ops_prcdns = {}
        self.max_prcdns = -1
        #Init  op array dictionary
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        module = __import__('operations')
        with open(os.path.join(cur_dir,'app.json')) as json_file:
            tmp  = json.load(json_file)
            ops = tmp['operations']
            for k,v in ops.items():
                    class_ = getattr(module, k)
                    instance = class_()
                    v = int(v)
                    if v < 0:
                        raise Exception("precedense must be greater then 1")
                    instance.set_precedence = v
                    self.op_dic[instance.symbol()] = instance
                    if  v in self.ops_prcdns:
                        self.ops_prcdns[v].append(instance.symbol())
                    else:
                        self.ops_prcdns[v] = [instance.symbol()]
                    self.max_prcdns = np.maximum(self.max_prcdns,v)

    def __parse_float__(self,s:str):
        try:
            return float(s)
        except:
            return None

    def calc(self,s:str)->float:
        s=s.replace(' ',"")
        ErrorWhileParse = False
        for i in range(0,self.max_prcdns+1,1):
            if i in self.ops_prcdns:
                for op in self.ops_prcdns[i]:
                    index = s.rfind(op)
                    if index >= 0:
                        try:
                            tmp1 = self.calc(s[:index])
                            tmp2 = self.calc(s[index+1:])
                            return self.op_dic[op].calc(tmp1,tmp2)
                        except:
                            return None

        i=0
        val = None
        while i < len(s):
            if s[i].isdigit():
                # There may be more than one
                # digits in the number.
                cnt=1
                while i+cnt < len(s) and (s[i+cnt].isdigit() or s[i+cnt] == '.'):
                    cnt += 1 
                val  = self.__parse_float__(s[i:+cnt])
                i=i+cnt
                ErrorWhileParse = (val == None)
                if ErrorWhileParse:
                    val = None
                i+=1
        return val

    def calc_file(self,path:str):
        with open(path) as data:
            lines = data.readlines()
            for s in lines:
                s = s.replace(" ","")
                index = s.find("=")
                if  index > 0:
                    print(s[:index+1] + str(self.calc(s[index+1:])))
                else:
                    print("Bad file format in line:" + s)
if __name__ == "__main__":    
    c=calculator()
    print(c.calc("1++"))
    # c.calc_file(r"./input.txt")
    