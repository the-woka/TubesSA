def cut_rod(price, n):
    total_value = 0
    selected_cuts = []

    while n > 0:
        max_val = float('-inf')
        best_cut = 0

        for i in range(1, n + 1):
            if price[i - 1] > max_val:
                max_val = price[i - 1]
                best_cut = i

        selected_cuts.append(best_cut)
        total_value += max_val
        n -= best_cut

    return total_value, selected_cuts


#example usage
input_price = input("Masukkan harga (dipisahkan spasi): ")
price = list(map(int, input_price.split()))
rod_length = len(price)
max_value, selected_cuts = cut_rod(price, rod_length)
print("Greedy Approach - Maximum value:", max_value)
print("Selected cuts:", selected_cuts)