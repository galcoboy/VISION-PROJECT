# VISION-PROJECT
Segment Studio – אשף קלאסטרים עם K-Means ו‑LLM
​
Segment Studio הוא כלי אינטראקטיבי לקלאסטרינג: מעלים קובץ CSV, מריצים K-Means עם ניתוח Elbow אוטומטי, ואז מייצרים שמות ותיאורים קריאים לקבוצות בעזרת מודל שפה (LLM).
​

תכונות עיקריות
העלאה ותצוגה של קובצי CSV (עד 200MB) כטבלת Pandas DataFrame.
​

חישוב אוטומטי של WCSS ושרטוט גרף Elbow לבחירת מספר הקלאסטרים 
k
k.
​

קלאסטרינג באמצעות K-Means עם 
k
k לבחירת המשתמש ותצוגת ספירת פריטים בכל קלאסטר.
​

יצירת שמות ותיאורים טקסטואליים לכל קלאסטר בעזרת LLM (לדוגמה, על בסיס דאטהסט Iris).
​

ייצוא CSV מעודכן עם מזהה קלאסטר, שם ותיאור לכל שורה.
​

טכנולוגיות
Python

Pandas, scikit-learn (K-Means, חישוב WCSS, מדד Silhouette)
​

Streamlit כממשק וובי אינטראקטיבי.
​

אינטגרציה עם מודל LLM (למשל LLAMA) ליצירת טקסט.
​

התקנה והרצה
שכפול המאגר (Repository):

bash
git clone https://github.com/your-username/segment-studio.git
cd segment-studio
יצירת סביבת עבודה וירטואלית (מומלץ):

bash
python -m venv .venv
source .venv/bin/activate  # ב-Windows: .venv\Scripts\activate
התקנת חבילות:

bash
pip install -r requirements.txt
הרצת האפליקציה:

bash
streamlit run app.py
פתיחת הכתובת המקומית בדפדפן (Streamlit מציג URL לאחר ההרצה).

אופן שימוש
העלאת CSV

לחיצה על “Choose a CSV file” או גרירה ושחרור של הקובץ (למשל irisnolabel.csv).
​

בדיקת התצוגה הטבלאית כדי לוודא שהעמודות והערכים תקינים.
​

הרצת Elbow (WCSS)

קביעת Min k ו‑Max k (למשל 2–10) ולחיצה על “Run WCSS”.
​

הסתכלות על גרף ה‑Elbow כדי לבחור ערך 
k
k מתאים.
​

יצירת קלאסטרים

בחירת 
k
k ולחיצה על “Create clusters”.
​

צפייה בספירת פריטים בכל קלאסטר ובנתונים הנלווים.
​

יצירת שמות לקבוצות עם LLM

הפעלת שלב ה‑LLM לקבלת שם ותיאור לכל קלאסטר (למשל “Iris Species”, “Petal Characteristics”).
​

ייצוא התוצאות

הורדת קובץ CSV מעודכן עם מזהי קלאסטר, שמות ותיאורים (למשל originalnameclustered.csv).
​
