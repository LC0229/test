
import chatgpt as cg
import json
import biosearch as ba
import csv



if __name__ == "__main__":
    chat = cg.Chatbot(cg.api_Key)
    term = input("what keywords you would like to search? ")
    base_url = 'https://pubmed.ncbi.nlm.nih.gov/?term='+str(term)
    all_articles = []
        
    for page in range(1, 5):  
        if(page==1):
            base_url = base_url
        else:
            base_url = base_url + "&page="+ str(page)
        
        articles = ba.__crawler_article__(base_url)
        all_articles.extend(articles)

    csv_path = "related_articles.csv"
        
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["title","authors","pmid","link"])
        writer.writeheader()
        for article in all_articles:
            writer.writerow(article)

            
            

    