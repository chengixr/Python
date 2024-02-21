import sys

userName = input('欢迎使用本系统，请输入您的姓名:')
money = 5000000


def cheekBalance():
    global money
    print(f'您的余额是:{money}')
    input('按任意键返回：')
    mainMenu()


def saveAccount():
    global money
    save_money = input('请输入存款金额:')
    while not save_money.isdigit():
        save_money = input('请输入正确的金额：')
    money += float(save_money)
    cheekBalance()
    input('按任意键返回：')
    mainMenu()


def withdrawMoney():
    global money
    withdraw_money = input('请输入取款金额:')
    while not withdraw_money.isdigit():
        withdraw_money = input('请输入正确的金额：')
    money -= float(withdraw_money)
    cheekBalance()
    input('按任意键返回：')
    mainMenu()


def mainMenu():
    print(f'{userName}，您好，请选择：')
    userSelcet = input('查询余额\t请按1\n存款\t\t请按2\n取款\t\t请按3\n结束服务\t请按4\n')
    while userSelcet not in ('1', '2', '3', '4'):
        input('请重新输入：')
    if userSelcet == '4':
        sys.exit(0)
    elif userSelcet == '1':
        cheekBalance()
    elif userSelcet == '2':
        saveAccount()
    elif userSelcet == '3':
        withdrawMoney()


if __name__ == '__main__':
    mainMenu()
