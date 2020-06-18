
if __name__ == '__main__':

    while True:
        print("*" * 30)
        print('栅栏密码实验：1、加密   2、解密  3、退出：')
        choose = input('请选择序号：')

        if (choose == '1'):  # encode
            plaintext = input('请输入要加密的消息: ')
            result = ''
            n = len(plaintext)
            i = 0
            j = 0
            while i < round(n / 2):
                result += plaintext[j]
                i += 1
                j += 2
            j = 1
            while i < n:
                result += plaintext[j]
                i += 1
                j += 2
            print('加密结果: ' + result)

        elif (choose == '2'):  # decode
            ciphertext = input('请输入要解密的密文: ')
            n = len(ciphertext)
            result = [None] * n
            i = 0
            j = 0
            while i < round(n / 2):
                result[j] = ciphertext[i]
                i += 1
                j += 2
            j = 1
            while i < n:
                result[j] = ciphertext[i]
                i += 1
                j += 2
            plaintext = ''
            for item in result:
                plaintext += item
            print('解密结果: ' + plaintext)

        elif (choose == '3'):
            print('退出成功')
            break

        else:
            print('错误，请选择1、2或3中的一个!')
            continue