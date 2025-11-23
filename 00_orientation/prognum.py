# フィボナッチ数列の「n番目」の数値を返す関数
def fibonacci(n):

    # 1番目(1) と 2番目(2) は、どちらも結果が 1 なのでまとめる
    if n <= 2:
        return 1

    # 3番目以降は、「直前の2つの和」
    return fibonacci(n - 1) + fibonacci(n - 2)