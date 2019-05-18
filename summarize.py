"""
Summarize data.
"""
import pickle


def main():
    print('Summary:')
    ids = pickle.load(open('ids.pkl','rb'))
    tweets = pickle.load(open('raw_tweets.pkl','rb'))
    print("Total Number of Users collected:",len(ids))
    print("Total Number of Tweets collected:",len(tweets))
    
    cluster_result = open('cluster_results.txt','r')
    print(cluster_result.read())
    
    classify_result = open('classify_result.txt','r')
    print(classify_result.read())
    
    f = open('summary.txt','w')
    f.write('Summary:')
    f.write("Total Number of Users collected:%d" %len(ids))
    f.write("Total Number of Tweets collected:%d" %len(tweets))
    f.write(cluster_result.read())
    f.write(classify_result.read())
    cluster_result.close()
    classify_result.close()
    f.close()
    
    
if __name__ == "__main__":
    main()