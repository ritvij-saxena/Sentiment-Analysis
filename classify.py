from nltk.sentiment import SentimentIntensityAnalyzer
import pickle

def sentimentAnalysis(data):
    sentiment = SentimentIntensityAnalyzer()
    result = []
    for i in data:
        result_dict = {}
        d = sentiment.polarity_scores(i)
        result_dict['text'] = i
        result_dict['scores'] = d
        result.append(result_dict)
    return result
        
def main():
    nltk.download('vader_lexicon')
    print('Getting tweets')
    all_data = pickle.load(open('tweets_text.pkl','rb'))
    print('Data collected')
    print('Classifying')
    value = sentimentAnalysis(all_data)
    neg = []
    pos = []
    neu = []
    
    for v in value:
        if v['scores']['neg'] > v['scores']['pos'] or v['scores']['neg'] > v['scores']['neu']:
            neg.append(v['text'])
        elif v['scores']['pos'] > v['scores']['neg'] or v['scores']['pos'] > v['scores']['neu']:
             pos.append(v['text'])
        else:
            neu.append(v['text'])
            
    print("Total Instances: %d" %len(value))
    print("No of Positive Instance: %d" %len(pos))
    print("No of Negative Instance: %d" %len(neg))
    print("No of Neutral Instance: %d" %len(neu))
    
    
    print('Saving results to classify_result.txt')
    f = open("classify_result.txt",'w')
    f.write("No of Positive Instance: %d \n" %len(pos))
    f.write("No of Negative Instance: %d \n" %len(neg))
    f.write("No of Neutral Instance: %d \n" %len(neu))
    f.write("\nExample of positive instances \n")
    for i in range(1,3):
        f.write("%d. "%i)
        f.write("%s\n"%pos[i-1])
    f.write("\n Example of negative instances \n")
    for i in range(1,3):
        f.write("%d. "%i)
        f.write("%s\n"%neg[i-1])
    f.write("\n Example of neutral instances \n")
    for i in range(1,3):
        f.write("%d. "%i)
        f.write("%s\n"%neu[i-1])
    f.close()
    
    f = open("all_classified_tweets.txt",'w')
    f.write("Positive Tweets \n")
    for i in range(1,len(pos)+1):
        f.write("%d. " %i)
        f.write("%s \n" %pos[i-1])
    
    f.write("\n \nNegative Tweets: \n")
    for i in range(1,len(neg)+1):
        f.write("%d. " %i)
        f.write("%s \n" %neg[i-1])
    
    f.write("\n \nNeutral Tweets: \n")
    for i in range(1,len(neu)+1):
        f.write("%d. " %i)
        f.write("%s \n" %neu[i-1])
    f.close()
    
    print('Completed')
if __name__ == "__main__":
    main()