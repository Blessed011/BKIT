import requests
import matplotlib.pyplot as plt

def create_url(main_url: str, number_amount: int) -> str:
    base_url = main_url
    final_url = f"{base_url}/num/{number_amount}"
    return final_url

def get_info(*, main_url: str, number_amount: int) -> str:
    final_url = create_url(main_url, number_amount)
    res = requests.get(final_url)
    return res.text

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    y = get_info(main_url=url, number_amount=int(input('Enter the number of Fibonacci elements: '))).split(', ')
    print(y)
    print(len(y))
    x = list(range(1, len(y) + 1))
    fig = plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('The first {} Fibonacci elements on the bar'.format(len(y)))
    plt.show()
    plt.plot(x, y)
    plt.scatter(x, y)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('The first {} Fibonacci elements on the graph'.format(len(y)))
    plt.show()
