import numpy as np
import string

#生成密码本和反密码本
def generate_table():
    # 获取“a”到”z“的顺序字符表
    pT = tuple(string.ascii_lowercase)

    # 建立随机化的密文字符表
    cT = []
    temp = np.random.permutation(26)
    for x in temp:
        cT.append(pT[x])

    # 建立密码本，即明文、密文对照表，这里使用了字典结构
    keyTable = {}
    for x, y in zip(pT, cT):
        keyTable[x] = y
    valueTable = {v: k for k, v in keyTable.items()}

    return [keyTable,valueTable]


if __name__ == '__main__':
    hasTable = False
    keyTable = {}
    valueTable = {}
    while True:
        print("*" * 30)
        print('置换密码实验：1、生成随机密码本   2、加密   3、解密  4、退出：')
        choose = input('请选择序号：')
        if (choose == '1'):
            [keyTable, valueTable] = generate_table()
            hasTable = True
            print('生成随机密码本成功！')

        elif (choose == '2'):  # encode
            if hasTable == False:
                print('请先生成随机密码本')
                continue
            plaintext = input('请输入要加密的消息（仅限英文字母）: ')
            result = ''
            for c in plaintext:
                result += keyTable[c]
            print('加密结果: ' + result)

        elif (choose == '3'):  # decode
            if hasTable == False:
                print('请先生成随机密码本')
                continue
            ciphertext = input('请输入要解密的密文: ')
            result = ''
            for c in ciphertext:
                result += valueTable[c]
            print('解密结果: ' + result)

        elif (choose == '4'):
            print('退出成功')
            break

        else:
            print('错误，请选择1、2或3中的一个!')
            continue