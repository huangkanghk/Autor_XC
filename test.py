# # #print('''へ　　　　　／|
# # 　　/＼7　　　 ∠＿/
# # 　 /　│　　 ／　／
# # 　│　Z ＿,＜　／　　 /`ヽ
# # 　│　　　　　ヽ　　 /　　〉
# # 　 Y　　　　　`　 /　　/
# # 　ｲ●　､　●　　⊂⊃〈　　/
# # 　()　 へ　　　　|　＼〈
# # 　　>ｰ ､_　 ィ　 │ ／／
# # 　 / へ　　 /　ﾉ＜| ＼＼
# # 　 ヽ_ﾉ　　(_／　 │／／
# # 　　7　　　　　　　|／
# # 　　＞―r￣￣`ｰ―＿''')
# question=input('您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
# if question=='需要':
#     subquestion=input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
#     if int(subquestion)==1:
#         print('推荐你去存取款窗口')
#     elif int(subquestion)==3:
#         print('推荐你去咨询款窗口')
#     elif int(subquestion)==2:
#         print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
#         number=input('请问您需要兑换多少金加隆呢？')
#         print('好的，我知道了，您需要兑换'+number+'金加隆')
#         print('那么，您需要付给我'+str(int(number)*51.3)+'人民币')
# else:
#     print('好的，再见！')
import os
print( os.path.dirname(__file__))