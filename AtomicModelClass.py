class AtomicModelClass:
    def ExtTransFn(self, input_event):
        pass
    
    def IntTransFn(self):
        pass

    def OutputFn(self):
        pass

    def TimeAdvancedFn(self):
        pass

class UnitAtomicModel(AtomicModelClass):
    inputSets = ['in1', 'in2']
    outputSets = ['out1', 'out2']
    statusSets = ['wait', 'move']

    def __init__(self, status, time):
        self.status = status
        self.time = time

    def ExtTransFn(self, input_event): #외부상태 천이함수 / 입력사건으로 인해  상태를 변화시키고 특정 기능을 실행
        if input_event == self.inputSets[0]:
            self.status = 'move'
            print("in1 is inserted, status is changed to", self.status)
            
        elif input_event == self.inputSets[1]:
            self.status = 'wait'
            print("in2 is inserted, status is changed to", self.status)
        else:
            print("error")

    def IntTransFn(self): #내부상태 천이함수 / 입력에 들어오면 상태를 변화시키고 특정 기능을 실행
        if self.status == 'wait':
            self.status = 'wait'
            print("status is not changed, now status is", self.status)
        elif self.status == 'move':
            self.status = 'wait'
            print("satus is changed to", self.status)
        else:
            print("error")


    def OutputFn(self): #출력함수 / 상태가 변화하면서 출력이 발생
        if self.status == 'wait':
            self.status = 'wait'
            print("status is wait, so output is not presented")
        elif self.status == 'move':
            self.status = 'wait'
            print("satus is changed to", self.status, "and output event is occured with", self.outputSets[0])
        else:
            print("error")

    def TimeAdvancedFn(self):
        pass
    

a = UnitAtomicModel('wait', 0)
a.ExtTransFn('in1')
a.IntTransFn()
a.OutputFn()
