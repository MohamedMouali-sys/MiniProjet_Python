import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
df = pd.read_csv('Student Depression Dataset.csv')

# Afficher les 5 premières lignes
print(df.head())

# Infos générales sur le DataFrame
print(df.info())

# Statistiques de base
print(df.describe())

# Valeurs manquantes
print(df.isnull().sum())

# Sélection de colonnes spécifiques
print(df[['Age', 'Gender', 'Depression']])

# Filtrer : les étudiants dépressifs
depressed_students = df[df['Depression'] == 'Yes']
print(depressed_students)

# Créer une nouvelle colonne : "Age_Group"
df['Age_Group'] = pd.cut(df['Age'], bins=[15, 18, 22, 30], labels=['Teen', 'Young Adult', 'Adult'])
print(df[['Age', 'Age_Group']])

# Trier les données par Age décroissant
print(df.sort_values(by='Age', ascending=False))

# Moyenne, médiane, écart-type
print("Moyenne d'âge :", df['Age'].mean())
print("Médiane d'âge :", df['Age'].median())
print("Écart-type d'âge :", df['Age'].std())

# Grouper par Genre et calculer la moyenne d'âge
print(df.groupby('Gender')['Age'].mean())

# Grouper par Age_Group et compter les cas de dépression
print(df.groupby('Age_Group')['Depression'].value_counts())

# Histogramme de l'âge
df['Age'].hist(bins=10)
plt.title("Répartition de l'âge")
plt.xlabel("Âge")
plt.ylabel("Nombre d'étudiants")
plt.show()

# Courbe : nombre de cas de dépression par âge
df.groupby('Age')['Depression'].apply(lambda x: (x == 'Yes').sum()).plot()
plt.title("Cas de dépression par âge")
plt.xlabel("Âge")
plt.ylabel("Nombre de cas")
plt.show()

# Boxplot : âge selon la dépression
df.boxplot(column='Age', by='Depression')
plt.title("Âge par statut de dépression")
plt.suptitle("")
plt.xlabel("Dépression")
plt.ylabel("Âge")
plt.show()
