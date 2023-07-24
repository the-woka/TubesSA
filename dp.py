def cut_rod(price, n):
    val = [0] * (n + 1)
    cuts = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_val = float('-inf')
        best_cut = []
        for j in range(1, i + 1):
            if price[j - 1] + val[i - j] > max_val:
                max_val = price[j - 1] + val[i - j]
                best_cut = cuts[i - j] + [j]
        val[i] = max_val
        cuts[i] = best_cut

    return val[n], cuts[n]


# example usage
input_price = input("Masukkan harga (dipisah spasi): ")
price = list(map(int, input_price.split()))
rod_length = len(price)
max_value, selected_cuts = cut_rod(price, rod_length)
print("Dynamic Programming Approach - Maximum value:", max_value)
print("Selected cuts:", selected_cuts)
