# Rule Base Text Classification

In some cases, we may need to classify the text according to the words or characters in the sentence. In these cases, we can classify based on the word sets we have created. 6 tweets have been added to the project for testing. The tags are as follows.

<pre></preANGRY>ANGRY - changing_news10	irate hockey fan tases mayorβfor a cause http://t.co/fahteyvhr6  #news #angry #hockey #mayor #cause #charity
ANGRY - hey @pixarinsideout i am angry!!!!π‘π‘ #insideout #angry #drawing #color http://t.co/npywa76xs9
SAD - i can't stop listening to it's a sin lately. ππ­ππππ’π #sad #isolated #petheadproblems #mysummeriscrap
SAD - _justmonie rt @caroline_kodl: well i'm actually tired af. but i will not go to sleep without the follow. ππ #sad @caseymoreta
HAPPY - finally i have my ticket for the #comlondon π @vyrt @jaredleto #happy π http://t.co/2t4chaixui
HAPPY - glab: rt amy_laybourn: amazing weekend in amsterdam with marcus βοΈπβοΈπΉππ» #sun #holidays #happy #siteseeing #weekendaway π </pre>

We have 3 categories, these are "ANGRY, HAPPY, SAD", these categories are dynamically prepared with text files under the keyword folder. When trying to add a new category, the name of the category will be accepted as the name of the text file.

### **Output of Code**

Tweet: _justmonie rt @caroline_kodl: well i'm actually tired af. but i will not go to sleep without the follow. ππ #sad @caseymoreta

Category,Times

ANGRY = 0 , HAPPY = 0 , SAD = 2

**This tweet is SAD**

------------

Tweet: finally i have my ticket for the #comlondon π @vyrt @jaredleto #happy π http://t.co/2t4chaixui

Category,Times

ANGRY = 0 , HAPPY = 2 , SAD = 0

**This tweet is HAPPY**
