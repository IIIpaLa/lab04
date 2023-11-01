def count_common_elements(*lists):
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements.intersection_update(lst)
    return len(common_elements)

# Пример использования
list1 = [3, 2, 3, 4, 5]
list2 = [3, 1, 3, 4, 5]
list3 = [3, 2, 3, 4, 7]

common_count = count_common_elements(list1, list2, list3)
print("Количество общих элементов:", common_count)
