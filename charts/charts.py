import matplotlib.pyplot as plt

def pie_chart():
    label = ['A', 'B', 'C']
    values = [200, 385, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=label)
    plt.savefig('pie_chart.png')
    plt.close()