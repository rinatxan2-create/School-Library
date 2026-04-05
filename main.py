import pandas as pd

class SchoolLibraryProject:
    def __init__(self):
        # Бастапқы деректер базасы (CSV файлы ретінде сақтауға болады)
        self.data = pd.DataFrame(columns=['Student_Name', 'Class_Number', 'Class_Letter', 'Books_Read'])

    def add_student(self, name, class_num, class_let, books):
        """Жаңа оқушыны немесе оқылған кітап санын қосу"""
        new_row = {
            'Student_Name': name, 
            'Class_Number': int(class_num), 
            'Class_Letter': class_let, 
            'Books_Read': int(books)
        }
        self.data = pd.concat([self.data, pd.DataFrame([new_row])], ignore_index=True)
        print(f"Мәлімет қосылды: {name} ({class_num} '{class_let}' сыныбы)")

    def get_top_students(self, limit=5):
        """Мектеп бойынша ең көп кітап оқыған үздік оқушылар"""
        print(f"\n--- Мектеп бойынша ТОП {limit} оқушы ---")
        top = self.data.sort_values(by='Books_Read', ascending=False).head(limit)
        return top

    def get_class_rating(self):
        """Сыныптар рейтингі (қай сынып ең көп оқыды)展"""
        print("\n--- Сыныптар рейтингі ---")
        class_stats = self.data.groupby(['Class_Number', 'Class_Letter'])['Books_Read'].sum().reset_index()
        return class_stats.sort_values(by='Books_Read', ascending=False)

# Мысалы:
library = SchoolLibraryProject()

# Деректер енгізу (мысалы)
library.add_student("Холмирза Ринат", 11, "А", 15)
library.add_student("Есен Ахмед", 11, "Ә", 12)
library.add_student("Әлиева Аяжан", 9, "Б", 20)
library.add_student("Серікұлы Нұрым", 7, "А", 18)

# Нәтижелерді шығару
print(library.get_top_students())
print(library.get_class_rating())
