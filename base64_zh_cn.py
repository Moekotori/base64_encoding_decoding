import base64

while True:
    # 提示用户选择操作：加密、解密或退出
    z = input("你需要加密还是解密？加密输入1，解密输入2，退出请输入0: ")

    # 如果用户输入1，执行加密操作
    if z == '1':
        # 获取用户想要加密的内容
        zoe2 = input("请输入你要加密的内容: ")
        # 对用户输入的内容进行 UTF-8 编码，然后进行 base64 编码，并将结果解码回 UTF-8 字符串以便显示
        zoe2_encoded = base64.b64encode(zoe2.encode('utf-8')).decode('utf-8')
        # 打印加密后的内容
        print("加密后的内容是:", zoe2_encoded)

    # 如果用户输入2，执行解密操作
    elif z == '2':
        # 获取用户想要解密的内容
        zoe3 = input("请输入你要解密的内容: ")
        try:
            # 尝试对用户输入的内容进行 base64 解码，然后将结果解码回 UTF-8 字符串
            zoe3_decoded = base64.b64decode(zoe3).decode("utf-8")
            # 打印解密后的内容
            print("解密后的内容是:", zoe3_decoded)
        except Exception as e:
            # 如果解码过程中出现异常，打印错误信息
            print("解密失败，请确保输入的是正确的加密内容。错误信息:", str(e))

    # 如果用户输入0，退出程序
    elif z == '0':
        # 打印退出信息
        print("退出程序。")
        # 跳出循环，导致程序结束
        break

    # 如果用户输入不是1、2或0，提示输入错误
    else:
        # 打印错误提示信息
        print("输入错误，请输入1或2进行加密或解密，0退出。")

#Poweredbyzoe  ฅ•̀∀•́ฅ
