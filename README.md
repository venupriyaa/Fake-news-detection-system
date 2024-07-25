# FAKE NEWS DETECTION SYSTEM 

The Fake News Detection System aims to automatically distinguish between genuine and fake news articles. Utilizing natural language processing (NLP) and machine learning techniques, the system analyzes news content to classify it as either real or fake. This tool is critical in combatting the spread of misinformation and promoting media literacy. The project uses datasets from Kaggle, which include both labeled (true/false) and unlabeled data for training and testing the models.

## Requirements
Programming Language: Python 3.x
<br> Libraries:
* Pandas: For data manipulation and analysis (pip install pandas)
* NumPy: For numerical computations (pip install numpy)
* NLTK: For natural language processing tasks (pip install nltk)
* scikit-learn: For machine learning algorithms and model evaluation (pip install scikit-learn)
* Flask: For web application development (pip install flask)
* Matplotlib & Seaborn: For data visualization (pip install matplotlib seaborn)

## Additional Tools and Technologies
* CountVectorizer: To convert text data into vectors for machine learning models.
* TF-IDF Vectorizer: To transform text data by considering the frequency of words across documents.
* Machine Learning Models: Logistic Regression, SVM, Naïve Bayes, and others for classification tasks.
* Data Preprocessing: Techniques such as tokenization, lemmatization, and stopword removal.

This system not only classifies news articles but also provides an interactive web interface for users to input news text and receive a classification prediction. The accuracy of various classifiers is evaluated and compared to select the most effective model.
