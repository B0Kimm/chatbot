  
import os

from com_sba_api.utils.file_helper import FileReader
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score

from pathlib import Path
# dtree, rforest, nb, knn, svm,  


class UserService:
    def __init__(self):
        self.fileReader = FileReader()  
        self.data = os.path.abspath("api/chatbot_api/order/data")
        self.odf = None

    def hook(self):
        train = 'train.csv'
        test = 'test.csv'
        this = self.fileReader
        this.train = self.new_model(train) # payload
        this.test = self.new_model(test) # payload
        
        '''
        Original Model Generation
        '''
        self.odf = pd.DataFrame(

            {
             'userid' : this.train.PassengerId,
             'password' : '1',
             'name' : this.train.Name
             }
        )
        
        this.id = this.test['PassengerId'] # This becomes a question. 
        # print(f'Preprocessing Train Variable : {this.train.columns}')
        # print(f'Preprocessing Test Variable : {this.test.columns}')
        this = self.drop_feature(this, 'Cabin')
        this = self.drop_feature(this, 'Ticket')
        # print(f'Post-Drop Variable : {this.train.columns}')
        this = self.embarked_norminal(this)
        # print(f'Preprocessing Embarked Variable: {this.train.head()}')
        this = self.title_norminal(this)
        # print(f'Preprocessing Title Variable: {this.train.head()}')
        # name 변수에서 title 을 추출했으니 name 은 필요가 없어졌고, str 이니 
        # 후에 ML-lib 가 이를 인식하는 과정에서 에러를 발생시킬것이다.
        this = self.drop_feature(this, 'Name')
        this = self.drop_feature(this, 'PassengerId')
        this = self.age_ordinal(this)
        # print(f'Preprocessing Age Variable: {this.train.head()}')
        this = self.drop_feature(this, 'SibSp')
        this = self.sex_norminal(this)
        # print(f'Preprocessing Sex Variable: {this.train.head()}')
        this = self.fareBand_nominal(this)
        # print(f'Preprocessing Fare Variable: {this.train.head()}')
        this = self.drop_feature(this, 'Fare')
        # print(f'Preprocessing Train Result: {this.train.head()}')
        # print(f'Preprocessing Test Result: {this.test.head()}')
        # print(f'Train NA Check: {this.train.isnull().sum()}')
        # print(f'Test NA Check: {this.test.isnull().sum()}')
        this.label = self.create_label(this) # payload
        this.train = self.create_train(this) # payload
        # print(f'Train Variable : {this.train.columns}')
        # print(f'Test Variable : {this.train.columns}')
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        
        # print(this)
        df = pd.DataFrame(

            {
             'pclass': this.train.Pclass,
             'gender': this.train.Sex, 
             'age_group': this.train.AgeGroup,
             'embarked' : this.train.Embarked,
             'rank' : this.train.Title
             }
        )
     
        # print(self.odf)
        # print(df)
        sumdf = pd.concat([self.odf, df], axis=1)
        
        '''
userid password                                               name  pclass  gender age_group  embarked  rank
0         1        1                            Braund, Mr. Owen Harris       3       0         4         1     1
1         2        1  Cumings, Mrs. John Bradley (Florence Briggs Th...       1       1         6         2     3
2         3        1                             Heikkinen, Miss. Laina       3       1         5         1     2
3         4        1       Futrelle, Mrs. Jacques Heath (Lily May Peel)       1       1         5         1     3
4         5        1                           Allen, Mr. William Henry       3       0         5         1     1
..      ...      ...                                                ...     ...     ...       ...       ...   ...
886     887        1                              Montvila, Rev. Juozas       2       0         5         1     6
887     888        1                       Graham, Miss. Margaret Edith       1       1         4         1     2
888     889        1           Johnston, Miss. Catherine Helen "Carrie"       3       1         2         1     2
889     890        1                              Behr, Mr. Karl Howell       1       0         5         2     1
890     891        1                                Dooley, Mr. Patrick       3       0         5         3     1
[891 rows x 8 columns]
        
        '''
        return sumdf
        

