print("********************************")
print("*        分压电阻适配器        *")
print("* Author  -> EasyBlue          *")
print("* Version -> 1.0               *")
print("* Date    -> 2022.12.1         *")
print("********************************")
print("\n")
import copy,os,random
RList1 = [1.0, 1.1, 1.2, 1.3, 1.38, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.236, 6.8, 7.5, 8.2, 9.1, 10.0, 10.2, 10.5, 10.7, 11.0, 11.3, 11.5, 11.8, 12.0, 12.1, 12.4, 12.7, 13.0, 13.3, 13.7, 14.0, 14.3, 14.7, 15.0, 15.4, 15.8, 16.0, 16.2, 16.5, 16.9, 17.4, 17.8, 18.0, 18.2, 18.7, 19.0, 19.1, 19.6, 20.0, 20.5, 21.0, 22.0, 24.0, 27.0, 30.0, 33.0, 33.2, 34.0, 34.8, 35.7, 36.0, 36.5, 37.4, 38.3, 39.0, 39.2, 40.2, 42.2, 43.0, 44.2, 45.3, 46.4, 47.0, 47.5, 48.2, 48.7, 49.9, 51.0, 51.1, 52.3, 53.6, 54.9, 56.0, 56.2, 57.6, 59.0, 60.4, 61.9, 62.0, 68.0, 75.0, 82.0, 91.0, 100.0, 102.0, 105.0, 107.0, 110.0, 113.0, 115.0, 118.0, 120.0, 121.0, 124.0, 127.0, 130.0, 133.0, 137.0, 140.0, 143.0, 147.0, 150.0, 154.0, 158.0, 160.0, 162.0, 165.0, 169.0, 174.0, 178.0, 180.0, 182.0, 187.0, 191.0, 196.0, 200.0, 205.0, 210.0, 220.0, 240.0, 270.0, 300.0, 330.0, 332.0, 340.0, 348.0, 350.0, 357.0, 360.0, 365.0, 374.0, 383.0, 390.0, 392.0, 402.0, 412.0, 422.0, 430.0, 432.0, 442.0, 453.0, 464.0, 470.0, 475.0, 487.0, 499.0, 510.0, 511.0, 523.0, 536.0, 549.0, 560.0, 562.0, 565.0, 578.0, 590.0, 604.0, 619.0, 620.0, 680.0, 750.0, 820.0, 910.0, 1000.0, 1020.0, 1050.0, 1070.0, 1100.0, 1130.0, 1150.0, 1180.0, 1200.0, 1210.0, 1240.0, 1270.0, 1300.0, 1330.0, 1341.2, 1370.0, 1400.0, 1430.0, 1470.0, 1500.0, 1540.0, 1580.0, 1600.0, 1620.0, 1650.0, 1690.0, 1740.0, 1780.0, 1800.0, 1820.0, 1870.0, 1910.0, 1960.0, 2000.0, 2050.0, 2100.0, 2200.0, 2400.0, 2700.0, 3000.0, 3200.0, 3300.0, 3320.0, 3400.0, 3480.0, 3570.0, 3600.0, 3650.0, 3740.0, 3830.0, 3900.0, 3920.0, 4019.9999999999995, 4120.0, 4220.0, 4300.0, 4320.0, 4420.0, 4530.0, 4640.0, 4700.0, 4750.0, 4870.0, 4990.0, 5100.0, 5110.0, 5230.0, 5360.0, 5490.0, 5600.0, 5620.0, 5760.0, 5900.0, 6040.0, 6190.0, 6200.0, 6340.0, 6490.0, 6600.0, 7500.0, 8200.0, 9100.0, 10000.0, 10500.0, 10700.0, 11000.0, 11300.0, 11500.0, 11800.0, 12000.0, 12100.0, 12400.0, 12700.0, 13000.0, 13300.0, 13700.0, 14000.0, 14300.0, 15000.0, 15400.0, 15800.0, 16000.0, 16200.0, 16500.0, 16900.0, 17400.0, 17800.0, 18000.0, 18200.0, 18700.0, 19600.0, 20000.0, 20500.0, 21000.0, 21500.0, 22000.0, 24000.0, 27000.0, 30000.0, 33000.0, 34000.0, 34800.0, 35700.0, 36000.0, 36500.0, 37400.0, 38300.0, 39000.0, 39200.0, 40200.0, 41200.0, 42200.0, 43000.0, 43200.0, 44200.0, 45300.0, 46400.0, 47000.0, 47500.0, 48700.0, 49900.0, 51000.0, 51100.0, 52300.0, 53600.0, 54900.0, 56000.0, 56200.0, 57600.0, 59000.0, 60400.0, 61900.0, 62000.0, 63400.0, 64900.00000000001, 68000.0, 75000.0, 82000.0, 91000.0, 100000.0, 107000.0, 110000.0, 113000.0, 115000.0, 118000.0, 120000.0, 121000.0, 124000.0, 127000.0, 130000.0, 133000.0, 137000.0, 140000.0, 143000.0, 147000.0, 150000.0, 154000.0, 158000.0, 160000.0, 162000.0, 165000.0, 169000.0, 174000.0, 178000.0, 180000.0, 182000.0, 187000.0, 191000.0, 196000.0, 200000.0, 205000.0, 210000.0, 215000.0, 220000.0, 221000.0, 240000.0, 270000.0, 300000.0, 330000.0, 357000.0, 360000.0, 365000.0, 374000.0, 383000.0, 390000.0, 392000.0, 402000.0, 412000.0, 422000.0, 430000.0, 432000.0, 442000.0, 453000.0, 464000.0, 470000.0, 475000.0, 487000.0, 499000.0, 510000.0, 511000.0, 523000.0, 536000.0, 549000.0, 560000.0, 562000.0, 576000.0, 590000.0, 604000.0, 619000.0, 620000.0, 634000.0, 649000.0, 665000.0, 680000.0, 681000.0, 750000.0, 820000.0, 910000.0, 1000000.0, 1100000.0, 1200000.0, 1300000.0, 1500000.0, 1600000.0, 1800000.0, 2000000.0, 2200000.0, 2400000.0, 2700000.0, 3000000.0, 3300000.0, 3600000.0, 3900000.0, 4300000.0, 4700000.0, 5100000.0, 5600000.0, 6200000.0, 6800000.0, 7500000.0, 8199999.999999999, 9100000.0, 10000000.0, 15000000.0, 22000000.0]
Err = 0.01
Rerr = 0.01
RMin = 0
Vout = 10
Vin = 20
Result = list()
Bestresult = list()

import winreg,platform

# Vout = Vint * Rout/(Rout+Rv)
def get_desktop():
    if "windows" in str(platform.platform()).lower():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        return winreg.QueryValueEx(key, "Desktop")[0]
    else:
        return "."


def RandomR(R,rerr):
    if random.randint(0,1):
        R = (1 + rerr * random.random()) * R
    else:
        R = (1 - rerr * random.random()) * R
    return R

# 阻值精度匹配
def RErrCompute(Rout,Rv,rerr):
    global Err,Rerr
    Rout = RandomR(Rout,rerr)
    Rv = RandomR(Rv,rerr)
    ret = abs(Vout - Vin * (Rout / (Rout + Rv)))
    if ret < (Vout * Err):
        return ret
    return False

# 匹配符合的电阻
def MatchingAccuracy(rerr):
    global Err,Rerr,RMin,Vout,Vin
    Ret = list()
    Length = len(RList1)
    Length = Length * Length
    Tick = int(Length / 100)
    count = 0
    for Rout in RList1:
        for Rv in RList1:
            count += 1
            if(count % Tick == 0):
                print("\rProgress:%d%%" % int(count/Tick) + str(["=" for i in range(int(count/Tick))]).replace("', '","").replace("'",""),end="")
            Temp = RErrCompute(Rout,Rv,rerr)
            if Temp:
                if RMin == 0:
                    Ret.append([Rout,Rv,copy.deepcopy(Temp)])
                else:
                    if Rout > RMin and Rv > RMin:
                        Ret.append([Rout,Rv,copy.deepcopy(Temp)])
    print()
    print("Successful to adapter");
    return Ret

# 最佳匹配
def BestMatching(RAccuracyList):
    global Err,Rerr,RMin,Vout,Vin
    count = 0
    Min = 100
    flag = 0
    for each in RAccuracyList:
        if each[2] < Min:
            Min = each[2]
            flag = count
        count+=1
    if flag != 0:
        return RAccuracyList[flag]
    else:
        return ['','','']

# 转换单位
def TransOum(Num):
    if 0 <= Num <= 999:
        return str(Num)
    elif 999 < Num <= 999999:
        return str(Num/1000) + "K"
    elif 999999 < Num <= 9999999999999:
        return str(Num/1000000) + "M"

# 显示匹配信息
def Display(RAccuracyList):
    global Err,Rerr,RMin,Vout,Vin
    if RAccuracyList == list():
        print("匹配列表为空,调整参数运行后在试")
        return
    print("匹配项")
    print("***************************************************************")
    print("*    输出电阻              串联电阻                误差       *")
    print("*                                                             *")
    for each in RAccuracyList:
        print("*      %-20s" % TransOum(each[0]),
        " %-17s" % TransOum(each[1]),
        "%-14.10Lf" % each[2],"*"
        )
    print("*                                                             *")
    print("*    输出电阻              串联电阻                误差       *")
    print("*                                                             *")
    print("***************************************************************")
    print()
    print("最佳匹配: " + TransOum(Bestresult[0]) + "   " + TransOum(Bestresult[1]) + "   "+ str(Bestresult[2]))

# 打印所有电阻
def ShowRList():
    flag = 0
    for each in RList1:
        print("%-6s" % TransOum(each),end=" ")
        if(flag % 10 == 0):
            print()
        flag += 1
    print()
    
# 本地保存
def SaveData():
    if Result == list():
        print("匹配列表为空,调整参数运行后在试")
        return
    SaveStr = ""
    with open(get_desktop() + "\\Resistance.txt",'w') as f:
        SaveStr += "     输出电阻        串联电阻                误差        \n"
        for each in Result:
            SaveStr += "      %-20s" % TransOum(each[0]) + " %-17s" % TransOum(each[1]) + "%-14.10Lf" % each[2] + "\n"
        SaveStr += "     输出电阻        串联电阻                误差        \n"
        SaveStr += "最佳匹配: " + TransOum(Bestresult[0]) + "   " + TransOum(Bestresult[1]) + "   "+ str(Bestresult[2]) + "\n\n"
        SaveStr += "输入电压[Vout]       : " + str(Vout) + "\n\n"
        SaveStr += "输出电压[Vin]        : " + str(Vin) + "\n\n"
        SaveStr += "电阻误差[Rerr]       : " + str(Rerr) + "\n\n"
        SaveStr += "最小电阻值[RMin]     : " + str(RMin) + "\n\n"
        SaveStr += "输出电压误差[Err]    : " + str(Err) + "\n\n"
        f.write(SaveStr)
    

def __BoolString(Isprint,Str):
    if Isprint:
        return Str
    return str()


def __IsVOK():
    return Vin > Vout and Vin > 0 and Vout > 0


def __OptionsMenu():
    print()
    print("\tErr                        %-25Lf%-10s" % (Err,"允许输出电压的误差"),end="\n\n")
    print("\tRerr                       %-25Lf%-10s" % (Rerr,"电阻自身的误差"),end="\n\n")
    print("\tRMin                       %-25Lf%-10s" % (RMin,"允许最小的阻值"),end="\n\n")
    print("\tVout             %s%s%-25Lf%-10s" % (__BoolString(__IsVOK(),"          "),__BoolString(not __IsVOK(),"[需要配置]"),Vout,"输出电压"),end="\n\n")
    print("\tVin              %s%s%-25Lf%-10s" % (__BoolString(__IsVOK(),"          "),__BoolString(not __IsVOK(),"[需要配置]"),Vin,"输入电压"),end="\n\n")


def __Helpmenu():
    print(" |help                    查看帮助")
    print(" |show options            查看配置信息")
    print(" |show                    查看适配输出")
    print(" |listr                   查看所有电阻值")
    print(" |set                     设置配置文件")
    print(" |run                     运行程序")
    print(" |save                    保存配置输出")


def __Wrong():
    print("Error > [指令有误,可使用help查看指令]")


def __ISSetOK(Param,Data):
    global Err,Rerr,RMin,Vout,Vin
    if Param == "Err":
        if 0 < float(Data) < 1:
            Err = float(Data)
            print("Err = %10Lf" % Err)
        else:
            raise Exception("Err不在(0,1)范围")

    elif Param == "Rerr":
        if 0 < float(Data) < 1:
            Rerr = float(Data)
            print("Rerr = %10Lf" % Rerr)
        else:
            raise Exception("Rerr不在(0,1)范围")
    
    elif Param == "RMin":
        if 0 <= float(Data):
            RMin = float(Data)
            print("RMin = %10Lf" % RMin)
        else:
            raise Exception("RMin不在[0,∞)范围")

    elif Param == "Vout":
        if 0 < float(Data):
            Vout = float(Data)
            print("Vout = %10Lf" % Vout)
        else:
            raise Exception("Vout不在(0,∞)范围")

    elif Param == "Vin":
        if 0 < float(Data):
            Vin = float(Data)
            print("Vin = %10Lf" % Vin)
        else:
            raise Exception("Vin不在(0,∞)范围")
    else:
        raise Exception("指令有误,可使用help查看指令")


def __SetFunc(Cmd):
    try:
        Cmd = Cmd.replace("set ","").split(" ")
        __ISSetOK(Cmd[0],Cmd[1])
    except IndexError as ex:
        print("Error > [需要两个参数]")
        print("eg: set Vout 10")
    except Exception as ex:
        print("Error > [" + str(ex) + "]")
        print("eg: set Vout 10")


def __Run():
    global Err,Rerr,RMin,Vout,Vin,Bestresult,Result
    Run = True
    if not 0 < Err < 1:
        print("Error  [Param(Err) -> 区间应在(0,1)]")
        Run = False
    if not 0 < Rerr < 1:
        print("Error  [Param(Rerr) -> 区间应在(0,1)]")
        Run = False
    if not 0 <= RMin:
        print("Error  [Param(RMin) -> 区间应在[0,∞)]")
        Run = False
    if not 0 < Vout:
        print("Error  [Param(Vout) -> 区间应在(0,∞)]")
        Run = False
    if not 0 < Vin:
        print("Error  [Param(Vin) -> 区间应在(0,∞)]")
        Run = False
    if Vout >= Vin:
        print("Error  [Param(Vin) 不能小于等于 Param(Vout)]")
        Run = False
    if not Run:
        return
    else:
        Result = MatchingAccuracy(Rerr)
        Bestresult = BestMatching(Result)
        

def __ExitTip():
    c = input("\n是否退出[y/n]")
    if c == 'y':
        exit()


def __Show():
    Display(Result)


def __DealCmd(Cmd):
    if Cmd.lower() == "show options":
        __OptionsMenu()
    elif Cmd.lower() == "help":
        __Helpmenu()
    elif Cmd.lower() == "run":
        __Run()
    elif Cmd.lower() == "clear":
        os.system("clear")
    elif Cmd.lower() == "cls":
        os.system("cls")
    elif Cmd.lower() == "show":
        __Show()
    elif Cmd.lower() == "listr":
        ShowRList()
    elif Cmd.lower() == "save":
        SaveData()
    elif "set " in Cmd.lower():
        __SetFunc(Cmd)
    else:
        __Wrong()
        

def __UserMenu():
    while True:
        try:
            Cmd = input("EzCmd > ")
            __DealCmd(Cmd)
        except KeyboardInterrupt:
            __ExitTip()


if __name__ == '__main__':
    __UserMenu()
