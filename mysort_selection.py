from tqdm import tqdm




def selection_sort(lst: list, flag: str):
    for i in tqdm(range(len(lst))):
        minimum = i

        for j in range(i + 1, len(lst)):
            # Выбор наименьшего значения
            if lst[j][flag] < lst[minimum][flag]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        lst[minimum][flag], lst[i][flag] = lst[i][flag], lst[minimum][flag]

    return lst