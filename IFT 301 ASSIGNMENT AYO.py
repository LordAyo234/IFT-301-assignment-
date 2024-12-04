import matplotlib.pyplot as plt
categories=['Spinach','Sausage','Prawns','Pineapple','Mushroom']
proportions=[0.28,0.18,0.08,0.28,0.16]
plt.figure(figsize=(8,6))
plt.barh(categories,proportions,color='red')
plt.xlabel('Proportion of Total')
plt.title('Proportion of Different Pizza Toppings')
plt.show()
