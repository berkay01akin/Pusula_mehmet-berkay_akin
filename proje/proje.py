import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


df = pd.read_excel("Talent_Academy_Case_DT_2025.xlsx")

df['UygulamaSuresi'] = df['UygulamaSuresi'].str.replace('Dakika', '', regex=False).astype(float)
df['TedaviSuresi'] = df['TedaviSuresi'].str.replace(' Seans', '', regex=False).astype(float)


df['KronikHastalikSayisi'] = df['KronikHastalik'].apply(
    lambda x: len(str(x).split(',')) if pd.notnull(x) and str(x).strip() != '' else 0
)
df['AlerjiSayisi'] = df['Alerji'].apply(
    lambda x: len(str(x).split(',')) if pd.notnull(x) and str(x).strip() != '' else 0
)


print("--- EDA Başlangıcı ---")

print("\nVerinin Genel Yapısı ve Eksik Değerler:")
print(df.info())

print("\nEksik Değerlerin Sayısı:")
print(df.isnull().sum())


print("\nSayısal Değişkenlerin Dağılımı (Histogram ve Kutu Grafiği):")
numeric_cols_for_eda = ['Yas', 'UygulamaSuresi', 'TedaviSuresi', 'KronikHastalikSayisi', 'AlerjiSayisi']
for col in numeric_cols_for_eda:
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'{col} Dağılımı')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.title(f'{col} Kutu Grafiği')
    plt.show()


print("\nKategorik Değişkenlerin Dağılımı (Çubuk Grafiği):")
categorical_cols_for_eda = ['Cinsiyet', 'KanGrubu', 'Uyruk', 'Bolum']
for col in categorical_cols_for_eda:
    plt.figure(figsize=(8, 5))
    sns.countplot(y=col, data=df, order=df[col].value_counts().index)
    plt.title(f'{col} Değişkeni Frekansları')
    plt.show()


print("\nDeğişkenler Arası İlişkiler (Korelasyon Isı Haritası):")
plt.figure(figsize=(10, 8))

correlation_matrix = df[numeric_cols_for_eda].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Sayısal Değişkenler Arası Korelasyon')
plt.show()

print("--- EDA Sonu ---")


target = 'TedaviSuresi'

X = df.drop(columns=[target, 'HastaNo', 'KronikHastalik', 'Alerji', 'Tanilar', 'TedaviAdi', 'UygulamaYerleri'])
y = df[target]


numeric_cols = ['Yas', 'UygulamaSuresi', 'KronikHastalikSayisi', 'AlerjiSayisi']
categorical_cols = [
    col for col in X.columns if col not in numeric_cols and X[col].dtype == 'object'
]


numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])


categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])


preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_pipeline, numeric_cols),
    ('cat', categorical_pipeline, categorical_cols)
], remainder='passthrough')


X_processed = preprocessor.fit_transform(X)

print("\nİşlenmiş Veri Boyutu:")

print(X_processed.shape)
