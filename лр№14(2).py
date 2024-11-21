import pandas as pd
import matplotlib.pyplot as plt

def visualize_education_data():
    """
    Візуалізація даних про дітей поза школою для України та США
    """
    # Штучні дані про дітей поза школою (молодша школа)
    data = {
        'Рік': range(2000, 2021),
        'Україна': [
            12.5, 11.8, 10.9, 10.2, 9.6, 9.0, 8.5, 8.1, 7.7, 7.3, 
            6.9, 6.5, 6.2, 5.9, 5.6, 5.3, 5.0, 4.8, 4.6, 4.4, 4.2
        ],
        'США': [
            5.2, 4.9, 4.7, 4.5, 4.3, 4.1, 3.9, 3.7, 3.5, 3.3,
            3.1, 2.9, 2.7, 2.5, 2.3, 2.1, 1.9, 1.7, 1.5, 1.3, 1.1
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Лінійний графік
    plt.figure(figsize=(12, 5))
    plt.plot(df['Рік'], df['Україна'], label='Україна', marker='o')
    plt.plot(df['Рік'], df['США'], label='США', marker='s')
    
    plt.title('Діти поза школою (молодша школа)')
    plt.xlabel('Рік')
    plt.ylabel('Відсоток дітей')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Стовпчаста діаграма
    country = input("Введіть назву країни (Україна/США): ")
    if country in df.columns:
        plt.figure(figsize=(10, 5))
        plt.bar(df['Рік'], df[country])
        plt.title(f'Діти поза школою в {country}')
        plt.xlabel('Рік')
        plt.ylabel('Відсоток дітей')
        plt.show()
    else:
        print("Невірна назва країни")

visualize_education_data()