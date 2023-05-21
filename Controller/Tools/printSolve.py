class printSolve():
    def print_cipher_and_solve(method, ciphertext, plaintext):
        print(f"被 {method} 編碼的資料為： '{ciphertext}' ")
        print()
        times = 3

        while times > 0:
            key = input("請輸入解碼後的結果(大小寫都可以)：")

            if key.upper() == plaintext or key.lower() == plaintext:
                print("成功！你答對了")
                print(f"經過 {method} 解碼後的數據為：{plaintext}")
                return
            else:
                times -= 1
                print(f"你還有{times}次機會")
        print(f"失敗！被解碼的結果應為 {plaintext}")