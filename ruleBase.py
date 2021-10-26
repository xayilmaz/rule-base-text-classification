#region Library
from os       import walk
from category import Category
from tabulate import tabulate
#endregion

#region Find Max Point Of Category
def FindMaxPointOfCategory(categories):
    maxPoint            = categories[0].point
    maxCategoryName     = ""
    sizeOfCategoryArray = len(categories)

    for i in range(0, sizeOfCategoryArray):
        if categories[i].point >= maxPoint:
            maxPoint         = categories[i].point
            maxCategoryName  = categories[i].nameOfCategory

    return maxCategoryName
#region Classifier
def Classifier(categories, text):

    for category in categories:
        for keyWord in category.categoryList:
            if keyWord in text:
                category.point += 1

    print(f"Tweet: {text}")

    resultOfClassification = []
    for category in categories:
        resultOfClassification.append([category.nameOfCategory, category.point])

    print(tabulate(resultOfClassification, headers=["Category", "Times"]))

    print(f"\nThis tweet is {FindMaxPointOfCategory(categories)}")
    print("----------------------------------------------------------------------------------------------------------")

    for category in categories:
        category.point = 0
#endregion

nameOfFilesList = []
for (dirPath, dirNames, fileNames) in walk("keyWord"):
    nameOfFilesList.extend(fileNames)
    break

categoriesObjectList = []
for n in nameOfFilesList:
    globals()['wordList%s' % n[:-4]] = open(f'keyWord/{n}', 'r', encoding="UTF-8").read().splitlines()
    globals()['category%s' % n[:-4]] = Category(n[:-4], globals()['wordList%s' % n[:-4]])
    categoriesObjectList.append(globals()['category%s' % n[:-4]])


receipts = open('tweet.txt', encoding="UTF-8").readlines()

for receipt in receipts:
    Classifier(categoriesObjectList, receipt)