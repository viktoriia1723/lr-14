import matplotlib.pyplot as plt

def create_educational_pie_chart():
    """
    Побудова кругової діаграми розподілу учнів за статтю
    """
    # Дані про розподіл учнів
    students_data = [52, 48]  # 52% хлопців, 48% дівчат
    labels = ['Хлопці', 'Дівчата']
    colors = ['lightblue', 'pink']
    
    plt.figure(figsize=(8, 6))
    plt.pie(
        students_data, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%',  # Відображення відсотків
        startangle=90,
        shadow=True
    )
    plt.title('Розподіл учнів за статтю')
    plt.axis('equal')  # Коло замість еліпса
    plt.show()

create_educational_pie_chart()