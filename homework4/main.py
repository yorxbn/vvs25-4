import pandas as pd

def analyze_dataset():
    titanic = pd.read_csv("titanic.csv")
    
    print("=" * 50)
    print(f"Первые 10 строк:")
    print(titanic.head(10))
    print("=" * 50)
    
    print("Статистика по возрасту:")
    print(titanic["Age"].describe())
    print("=" * 50)
    
    rows, cols = titanic.shape
    print(f"Размер: {rows} строк, {cols} столбцов")
    print("=" * 50)
    
    print("Пропуски в данных:")
    for col, count in titanic.isnull().sum().items():
        print(f"  {col}: {count}")
    print(f"Типы данных:\n{titanic.dtypes}")
    print("=" * 50)
    
    missing_before = titanic["Age"].isnull().sum()
    avg_age = titanic["Age"].mean()
    titanic["Age"] = titanic["Age"].fillna(avg_age)
    print(f"Заполнение пропусков в возрасте: {missing_before} → {titanic['Age'].isnull().sum()}")
    print(f"Средний возраст: {avg_age:.1f}")
    print("=" * 50)

def analyze_gender_stats():
    titanic = pd.read_csv("titanic.csv")
    males = titanic[titanic["Sex"] == "male"]
    females = titanic[titanic["Sex"] == "female"]
    
    male_surv = males[males["Survived"] == 1]
    male_rate = len(male_surv) / len(males) * 100
    print("МУЖЧИНЫ:")
    print(f"  Выжило: {male_rate:.1f}%")
    print(f"  Средний возраст: {males['Age'].mean():.1f}")
    print(f"  Выживших: {male_surv['Age'].mean():.1f}")
    print(f"  Погибших: {males[males['Survived']==0]['Age'].mean():.1f}")
    print("=" * 50)
    
    female_surv = females[females["Survived"] == 1]
    female_rate = len(female_surv) / len(females) * 100
    print("ЖЕНЩИНЫ:")
    print(f"  Выжило: {female_rate:.1f}%")
    print(f"  Средний возраст: {females['Age'].mean():.1f}")
    print(f"  Выживших: {female_surv['Age'].mean():.1f}")
    print(f"  Погибших: {females[females['Survived']==0]['Age'].mean():.1f}")
    print("=" * 50)
    
    men_filter = males[(males["Age"] > 30) & (males["Pclass"] == 1)]
    print(f"Мужчины >30 лет, 1 класс: {len(men_filter)} чел.")
    print("=" * 50)
    
    women_filter = females[(females["Age"] < 18) | (females["Survived"] == 1)]
    print(f"Женщины <18 лет или выжившие: {len(women_filter)} чел.")
    print("=" * 50)
    
    grouped = titanic.groupby(["Pclass", "Sex"]).agg(
        средний_возраст=("Age", "mean"),
        процент_выживших=("Survived", "mean"),
        средняя_цена=("Fare", "mean")
    )
    print("Статистика по классу и полу:")
    print(grouped)
    print("=" * 50)

print("АНАЛИЗ ДАТАСЕТА TITANIC")
analyze_dataset()
analyze_gender_stats()
