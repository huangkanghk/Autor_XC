class TestCaseInfo():
    """
    测试用例信息
    """
    def __init__(self,id="",name="",owner="",result="",starttime="",endtime="",secondsDuration="",erroinfo=""):
        self.id=id
        self.name=name
        self.owner=owner
        self.result=result
        self.starttime=starttime
        self.endtime=endtime
        self.secondsDuration=secondsDuration
        self.erroinfo=erroinfo