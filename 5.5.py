height = int(input())
weight = int(input())
k = round((weight / ((height / 100) ** 2)), 2)


def dictionary(k):
    categories = {
        k < 16: 'выраженный дефицит массы тела',
        16 <= k < 18.49: 'недостаточная масса тела',
        18.5 <= k < 24.99: 'норма',
        25 <= k < 29.99: 'избыточная масса тела',
        30 <= k < 34.99: 'ожирение первой степени',
        35 <= k < 39.99: 'ожирение второй степени',
        40 <= k: 'ожирение третьей степени'
    }
    for key in categories:
        if key:
            return categories[key]


print(dictionary(k))
